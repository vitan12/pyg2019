from app import app
from app.models import User, InTicket, OutTicket
from app import db

def createUsers():
    users = User.query.all()
    for u in users:
        current_session = db.object_session(u)
        current_session.delete(u)
        current_session.commit()
    supporter = User(name='Jeff', username='jeffk', email='jeffk@gmail.com', password='password', category=0)

    providerChurch = User(name ='Church Group', username='church', email='church@gmail.com', password='password', category=1)
    providerCompany = User(name='Organization', username='company', email='company@gmail.com', password='password', category=1)
    providerNonProfit = User(name='Nonprofit', username='nonprofit', email='nonprofit@gmail.com', password='password', category=1)

    receiver = User(name='Sofia', username='sofiam', email='sofiam@yahoo.com', password='password', category=2)
    db.session.bulk_save_objects([supporter, providerChurch, providerCompany, providerNonProfit, receiver])
    db.session.commit()

def createTickets():
    intickets = InTicket.query.all()
    for i in intickets:
        current_session = db.object_session(i)
        current_session.delete(i)
        current_session.commit()
        
    ticketFood = InTicket(identifier='123456', items="[{\r\n  \t\t\"item\": \"Canned Beans\",\r\n  \t\t\"category\": \"Food\",\r\n  \t\t\"quantity\": 3\r\n  \t},\r\n  \t{\r\n  \t\t\"item\": \"Spaghetti-O's\",\r\n  \t\t\"category\": \"Food\",\r\n  \t\t\"quantity\": 1\r\n  \t},\r\n  \t{\r\n  \t\t\"item\": \"Minestrone Soup\",\r\n  \t\t\"category\": \"Food\",\r\n  \t\t\"quantity\": 5\r\n  \t}\r\n  ]", giver='jeffk', receiver='church')
    ticketClothes = InTicket(identifier='234567', items='[{\r\n  \t\t\"item\": \"Shirt M\",\r\n  \t\t\"category\": \"Clothing\",\r\n  \t\t\"quantity\": 2\r\n  \t},\r\n  \t{\r\n  \t\t\"item\": \"Jeans 36x38\",\r\n  \t\t\"category\": \"Clothing\",\r\n  \t\t\"quantity\": 1\r\n  \t},\r\n  \t{\r\n  \t\t\"item\": \"Knit Sweater M\",\r\n  \t\t\"category\": \"Clothing\",\r\n  \t\t\"quantity\": 1\r\n  \t}\r\n  ]', giver='jeffk', receiver='company')
    ticketMisc = InTicket(identifier='345678', items='[{\r\n  \t\t\"item\": \"36oz Laundry Detergent\",\r\n  \t\t\"category\": \"Cleaning\",\r\n  \t\t\"quantity\": 2\r\n  \t},\r\n  \t{\r\n  \t\t\"item\": \"Drying Rack\",\r\n  \t\t\"category\": \"Misc.\",\r\n  \t\t\"quantity\": 1\r\n  \t},\r\n  \t{\r\n  \t\t\"item\": \"Bike\",\r\n  \t\t\"category\": \"Misc.\",\r\n  \t\t\"quantity\": 1\r\n  \t}\r\n  ]', giver='jeffk', receiver='nonprofit')
    
    db.session.bulk_save_objects([ticketFood, ticketClothes, ticketMisc])
    db.session.commit()

