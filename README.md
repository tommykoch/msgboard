## Python Flask Message Board for Lametric (for Google App Engine)

This is a very simple Python web applications serving a message board
and a JSON formated API for Lametric Apps (www.lametric.com).

The web application is based on the [Flask framework](http://flask.pocoo.org) and 
prepared for deployment on [Google App Engine](https://developers.google.com/appengine/).


## Requirements

You'll need the [App Engine Python SDK](https://developers.google.com/appengine/downloads)
as well as python 2.7 and [pip 1.4 or later](http://www.pip-installer.org/en/latest/installing.html).


## Run Locally

1. Install the [App Engine Python SDK](https://developers.google.com/appengine/downloads).
2. Install [Eclipse] (https://eclipse.org/).
3. Install [PyDev] (http://www.pydev.org/) plugin for Eclipse.
4. Download/clone this project and import in new Eclipse/Pydev project
5. Install flask + dependencies (local)

   ```
   cd <project>
   pip install -r requirements.txt -t lib
   ```
  
   Note: App Engine can only import libraries from inside your project directory.

6. Run this project locally from the command line:

   ```
   dev_appserver.py .
   ```

Visit the application [http://localhost:8080](http://localhost:8080)

See [the development server documentation](https://developers.google.com/appengine/docs/python/tools/devserver)
for options when running dev_appserver.


## Deploy
To deploy the application:

1. Use the [Admin Console](https://appengine.google.com) to create a
   project/app id. (App id and project id are identical)
1. Change application name in app.yaml then 
   [Deploy the application](https://developers.google.com/appengine/docs/python/tools/uploadinganapp) 
   with
   
   ```
   appcfg.py -A <your-project-id> --oauth2 update .
   ```
   
1. Congratulations!  Your application is now live at your-app-id.appspot.com


## Credits

based on 
 [appengine-flask-skeleton](https://github.com/GoogleCloudPlatform/appengine-flask-skeleton)
and inspired by 
 [Ogreman/whiteboard](https://github.com/Ogreman/whiteboard)
and by [kenkam/msgbrd](https://github.com/kenkam/msgbrd)

### Feedback

Star this repo if you find it useful. Use the github issue tracker to give
feedback on this repo.

## Author
Thomas Koch