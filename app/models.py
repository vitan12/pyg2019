from sqlalchemy import Column, Integer, String
from app.database import Base
import json
# is_authenticated
# This property should return True if the user is authenticated, i.e. they have provided valid credentials. (Only authenticated users will fulfill the criteria of login_required.)
# is_active
# This property should return True if this is an active user - in addition to being authenticated, they also have activated their account, not been suspended, or any condition your application has for rejecting an account. Inactive accounts may not log in (without being forced of course).
# is_anonymous
# This property should return True if this is an anonymous user. (Actual users should return False instead.)
# get_id()
# This method must return a unicode that uniquely identifies this user, and can be used to load the user from the user_loader callback. Note that this must be a unicode - if the ID is natively an int or some other type, you will need to convert it to unicode.


class User(Base):
    __tablename__ = 'Users'
    __table_args__ = {'extend_existing': True}
    name = Column(String())
    username = Column(String(), unique=True, primary_key=True)
    email = Column(String())
    password = Column(String())
    category = Column(Integer())
    tickets = Column(String()) # OutTicket
    items_requested = Column(String()) # Item
    def __init__(self, name=None, username=None, email=None, password=None, tickets=None, items_requested=None, category=None):
        self.name = name
        self.username = username
        self.email = email
        self.password = password
        self.tickets = tickets
        self.items_requested = items_requested
        self.category = category

    def __repr__(self):
        return '<User {}>'.format(self.username)    

class Item(Base):
    __tablename__ = 'Item'
    __table_args__ = {'extend_existing': True}

    name = Column(String(), primary_key = True, unique=True)
    quantity = Column(Integer())
    category = Column(String())
    def __init__(self, name=None, quantity=None, category=None):
        self.name = name
        self.quantity = quantity
        self.category = category

    def __repr__(self):
        return json.dumps({'item':self.name, 'quantity':self.quantity, 'category':self.category})

class InTicket(Base):
    __tablename__ = 'InTicket'
    __table_args__ = {'extend_existing': True}

    identifier = Column(String(6), primary_key = True)
    items = Column(String(), unique=True) # Item
    
    giver = Column(String()) # Who gave it
    receiver = Column(String()) # Who got it
    
    def __init__(self, identifier=identifier, items=items, giver=giver, receiver=receiver):
        self.identifier = identifier
        self.items = items
        self.giver = giver
        self.receiver = receiver

    def __repr__(self):
        return '<InTicket {}>'.format(self.identifier)    

class OutTicket(Base):
    __tablename__ = 'OutTicker'
    __table_args__ = {'extend_existing': True}

    identifier = Column(String(6), primary_key = True)
    items = Column(String(), unique=True) # Item
    
    giver = Column(String())
    receiver = Column(String())
    
    def __init__(self, identifier=identifier, items=items, giver=giver, receiver=receiver):
        self.identifier = identifier
        self.items = items
        self.giver = giver
        self.receiver = receiver
    
    def __repr__(self):
        return '<OutTicket {}>'.format(self.identifier)    