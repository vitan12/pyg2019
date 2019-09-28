from sqlalchemy import Column, Integer, String
from app.database import Base

# is_authenticated
# This property should return True if the user is authenticated, i.e. they have provided valid credentials. (Only authenticated users will fulfill the criteria of login_required.)
# is_active
# This property should return True if this is an active user - in addition to being authenticated, they also have activated their account, not been suspended, or any condition your application has for rejecting an account. Inactive accounts may not log in (without being forced of course).
# is_anonymous
# This property should return True if this is an anonymous user. (Actual users should return False instead.)
# get_id()
# This method must return a unicode that uniquely identifies this user, and can be used to load the user from the user_loader callback. Note that this must be a unicode - if the ID is natively an int or some other type, you will need to convert it to unicode.


class User(Base):
    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True}

    name = Column(String(), unique=True)
    username = Column(String(), primary_key=True)
    email = Column(String(), unique=True)
    password = Column(String())
    items_received = Column(String(), unique=True)  # Item
    items_requested = Column(String(), unique=True) # Item
    def __init__(self, name=None, username=None, email=None, password=None, items_received=None, items_requested=None):
        self.name = name
        self.username = username
        self.email = email
        self.password = password
        self.items_received = items_received
        self.items_requested = items_requested


    def __repr__(self):
        return '<User {}>'.format(self.username)    

class Item(Base):
    __tablename__ = 'Item'
    __table_args__ = {'extend_existing': True}

    name = Column(String(), primary_key = True, unique=True)
    quantity = Column(Integer(), unique=True)
    
    def __repr__(self):
        return '<Item {}>'.format(self.name)    

    def __init__(self, name=None, quantity=None):
        self.name = name
        self.quantity = quantity


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