from flask import render_template, flash, redirect
from app.forms import LoginForm, ItemEntryForm
from app import app, db
from app.models import User, InTicket, Item
from app.database import db_session as db
from app.init_db import createUsers, createTickets
import time

@app.route('/')
def index():
    return render_template("examples/index.html")


@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    createUsers()
    createTickets()
    form = LoginForm()
    html_to_render = 'login.html'
    ticket = InTicket.query.filter_by(identifier='123456').first()
    print()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()

        print(user.category)
        if user.category == 0:
            html_to_render = 'supporter.html'
        elif user.category == 1:
            html_to_render = 'provider.html'
        elif user.category == 2:
            html_to_render = 'receiver.html'
        else:
            html_to_render = 'login.html'

    return render_template(html_to_render, title='Sign In', form=form, ticketinfo = ticket.identifier)

@app.route('/provider')
def provider():
    pass

@app.route('/supporter', methods=['GET', 'POST'])
def supporter():
    form = ItemEntryForm()
    html_to_render = 'supporter.html'
    if form.submit():
        # oldItem = Item.query.filter_by(name='Sweater').first()
        # current_session = db.object_session(oldItem)
        # current_session.delete(oldItem)
        # current_session.commit()
        print("Hi")
        itemNew = Item(name=form.name.data, quantity=form.quantity.data, category=form.cat_select.data)
        db.add(itemNew)
        db.commit()
        itemCreated = Item.query.filter_by(name=form.name.data).first()
        print(itemCreated)
        print("i")
        return render_template(html_to_render, form=form, itemInfo = itemCreated.name)
    else:
        return render_template(html_to_render, form=form)

    

    # if form.validate_on_submit():
    #     ticketFood = InTicket(identifier='', items="[{\r\n  \t\t\"item\": \"Canned Beans\",\r\n  \t\t\"category\": \"Food\",\r\n  \t\t\"quantity\": 3\r\n  \t},\r\n  \t{\r\n  \t\t\"item\": \"Spaghetti-O's\",\r\n  \t\t\"category\": \"Food\",\r\n  \t\t\"quantity\": 1\r\n  \t},\r\n  \t{\r\n  \t\t\"item\": \"Minestrone Soup\",\r\n  \t\t\"category\": \"Food\",\r\n  \t\t\"quantity\": 5\r\n  \t}\r\n  ]", giver='jeffk', receiver='church')
    



@app.route('/receiver')
def receiver():
    pass