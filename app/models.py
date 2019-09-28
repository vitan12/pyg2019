from sqlalchemy import Column, Integer, String
from database import Base


# class User(Base):
#     __tablename__ = 'users'
#     id = Column(Integer, primary_key=True)
#     name = Column(String(50), unique=True)
#     email = Column(String(120), unique=True)

#     def __init__(self, name=None, email=None):
#         self.name = name
#         self.email = email

#     def __repr__(self):
#         return '<User %r>' % (self.name)

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