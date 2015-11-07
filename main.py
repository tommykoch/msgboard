"""`main` is the top level module for your Flask application."""

# Import the Flask Framework
from flask import Flask, request, session, redirect, url_for, render_template
from datetime import datetime
from collections import namedtuple
Message = namedtuple('Message', ['sender', 'message', 'date'])

app = Flask(__name__)
app.config.from_object('settings.Production')

MAX_MESSAGES = 3

# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.

messages = []  # list of Message(s)

def add_message(sender, message):
    """add a new message to the list of all messages
    trim list to MAX_MESSAGES if needed
    returns newly created Message (or None)
    """
    global messages  
    if message:
        msg = Message(sender, message,  datetime.now())
        messages.append(msg)
        if len(messages) > MAX_MESSAGES:
            messages = messages[-MAX_MESSAGES:]
        return msg


@app.route('/')
def index():
    """Return default page"""
    return render_template('master.html')


@app.route('/demo')
def add():
    """adds a test message"""
    add_message('demo', 'message')
    return 'OK: %d' % len(messages)


@app.route('/send', methods=['GET', 'POST'])
def send_message():
    """allow to send a message"""
    global messages
    if request.method == 'POST':
        message = request.form['text'].strip()
        sender = request.form['sender'].strip()
        _msg = add_message(sender, message)
        return redirect(url_for('show_messages'))
    else:
        return render_template('send.html')


@app.route('/lst')
def list_messages():
    """list all messages (TXT)"""
    return '%d messages: %s' % (len(messages), ",\n".join(messages))



@app.route('/latest')
def latest_message():
    """show latest message (JSON)"""
    import json
    latest = messages[-1] if len(messages) else None
    if latest:
        msg = latest.message
        if latest.sender:
            msg = ("%s: " % latest.sender) + msg
        if latest.date:
            now = datetime.now()
            delta = now-latest.date
            if delta.days==0:
                dstr = "heute %s" % latest.date.strftime('%H:%M')
            elif delta.days==1:
                dstr = "gestern %s" % latest.date.strftime('%H:%M')
            else:
                dstr = latest.date.strftime('%Y-%m-%d %H:%M')
            msg = msg + (" (%s)" % dstr)
    else:
        msg ="keine Nachrichten"
        
    output = {"frames": [{
                          "index": 0,
                          "text": msg,
                          "icon": "i43"
                        }]
              }
    return json.dumps(output)


@app.route('/show')
def show_messages():
    """show all messages"""
    return render_template('messages.html', messages=messages)


@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, Nothing at this URL.', 404


@app.errorhandler(500)
def application_error(e):
    """Return a custom 500 error."""
    return 'Sorry, unexpected error: {}'.format(e), 500
