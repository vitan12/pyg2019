# config.py
import os

# Enable Flask's debugging features. Should be False in production
DEBUG = True

# Enable protection against Cross-site Request Forgery (CSRF)
CSRF_ENABLED = True

basedir = os.path.abspath(os.path.dirname(__file__))

