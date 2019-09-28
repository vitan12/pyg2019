# app/__init__.py

from flask import Flask
import sqlite3
from flask_migrate import Migrate
from app import models
from flask import g
from config import Config
from app.database import init_db



DATABASE = '/path/to/database.db'


# Initialize the app
app = Flask(__name__, instance_relative_config=True)
app.config.from_object(Config)
init_db()
# Load the views
from app import views
