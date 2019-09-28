# app/__init__.py

from flask import Flask
import sqlite3
from flask_migrate import Migrate
from app import models
from flask import g
from config import Config
from app.database import init_db
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate



DATABASE = 'sqlite://///home/aneesh/Desktop/pyg2019/sqlite.db'


# Initialize the app
app = Flask(__name__, instance_relative_config=True)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
init_db()
# Load the views
from app import views
