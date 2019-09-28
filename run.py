# run.py
from app import app
import sqlite3
from sqlite3 import Error
import config

if __name__ == '__main__':
    app.run()

app.config.from_object('config') 