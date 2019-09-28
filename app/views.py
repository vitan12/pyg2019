from flask import render_template, flash, redirect
from app.forms import LoginForm
from app import app
from app.models import User
from app.database import db_session as db

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User('Joff', 'joff69', 'joff@gmail.com', 'fuck you')
        db.add(user)
        db.commit()
        user = User.query.filter_by(username = form.username.data).first()
        print(user)
    return render_template('login.html', title='Sign In', form=form)
