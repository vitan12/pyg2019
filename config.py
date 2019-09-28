# config.py
import os

# Enable Flask's debugging features. Should be False in production
DEBUG = True

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'