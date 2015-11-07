"""
settings.py
Configuration for Flask app
Important: Place your keys in the secret_keys.py module, 
           which should be kept out of version control.
"""
from secret_keys import CSRF_SECRET_KEY, SESSION_KEY


class Config(object):
    # Set secret keys for CSRF protection
    SECRET_KEY = CSRF_SECRET_KEY
    CSRF_SESSION_KEY = SESSION_KEY
    # Flask-Cache settings
    CACHE_TYPE = 'gaememcached'


class Testing(Config):
    TESTING = True
    DEBUG = True
    CSRF_ENABLED = True


class Production(Config):
    DEBUG = False
    CSRF_ENABLED = True