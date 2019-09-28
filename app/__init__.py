# app/__init__.py

from flask import Flask
import sqlite3
from flask_migrate import Migrate
from app import routes, models
from flask import g



DATABASE = '/path/to/database.db'


# Initialize the app
app = Flask(__name__, instance_relative_config=True)

# Load the views
from app import views
