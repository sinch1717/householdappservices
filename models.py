from flask_sqlalchemy import SQLAlchemy
from app import app
from flask_migrate import Migrate
from datetime import datetime

# database named db
db = SQLAlchemy(app)

# 1. Table: users
class Users(db.Model):
    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    role = db.Column(db.String(20), nullable = False) #customer, service_professional
    username = db.Column(db.String(20), unique = True, nullable = False)
    password = db.Column(db.String(20), nullable = False)
    email = db.Column(db.String(80),  unique = True, nullable = False)
    registration_date = db.Column(db.DateTime, default = datetime.utcnow)

    # Relationships
    customer = db.relationship('Customer', backref = 'user', uselist = False, cascade = "all, delete-orphan") #uselist = False can be used to have tru one-to-one relationship, casecade - if a user is deleted all the subsequent relationships in the other tables are deleted
    service_professional = db.relationship('ServiceProfessional', backref = 'user', uselist = False, cascade = "all, delete-orphan")
    notifications = db.relationship('Notification', backref = 'user')


# 2. Table: customers
class Customer(db.Model):
    __tablename__ = 'customers'

    customer_id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable= False)
    f_name = db.Column(db.String(50))
    l_name = db.Column(db.String(50))
    address = db.Column(db.String(255))
    # state = db.Column(db.String(50))
    # city = db.Column(db.String(50))
    pincode = db.Column(db.String(6))
    phone_number = db.Column(db.String(10))
    
    service_requests = db.relationship('ServiceRequest', backref = 'customer')
    reviews = db.relationship('Review', backref = 'customer')


# 3. Table: service_professionals
class ServiceProfessional(db.Model):
    __tablename__ = 'service_professionals'

    professional_id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id', nullable = False))
    service_type_id = db.Column(db.Integer, db.ForeignKey('service_types.service_type_id'), nullable = False)
    rating = db.Column(db.Float)
    experience = db.Column(db.Integer)
    price = db.Column(db.Float, nullable = False) #price set by professional for each service type
    service_name = db.Column(db.ForeignKey('service_types.name'), nullable = False)
    file_path = db.Column(db.String(255)) # storing the file path of the document verification PDF
    
    # user = db.relationship('User', backref = 'service_professional')
    service_type = db.relationship('ServiceType', backref = 'service_professional')
    service_requests = db.relationship('ServiceRequest', backref = 'professional')
    reviews = db.relationship('Review', backref = 'service_professional')



# 4. Table = services
class Service(db.Model):
    __tablename__ = 'services'

    service_id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    service_type_id = db.Column(db.Integer, db.ForeignKey('service_types.service_type_id'), nullable = False)
    name = db.Column(db.String(100), nullable = False)
    description = db.Column(db.Text)
    image = db.Column (db.String(255))

    service_requests = db.relationship('ServiceRequest', backref = 'service')
    service_professionals = db.relationship('ServiceProfessional', backref = 'service')


# 5. Table - service_requests
class ServiceRequest(db.Model):
    __tablename__ = 'service_requests'

    service_request_id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    service_id = db.Column (db.Integer, db.ForeignKey('services.service_id'), nullable = False)
    customer_id = db.Column (db.Integer, db.ForeignKey('customers.customer_id'), nullable = False)
    professional_id = db.Column (db.Integer, db.ForeignKey('service_professionals.professional_id'))
    date_of_request = db.Column(db.DateTime, default = datetime.utcnow)
    date_of_completion = db.Column(db.DateTime)
    status = db.Column(db.String(50), nullable = False, default = 'requested') #by default 'reqeusted' value assigned
    remarks = db.Column(db.Text)

    activities = db.relationship('Activity', backref = 'service_request')
    review = db.relationship('Review', backref = 'service_request', uselist = False)


# 6. Table - service_types
class ServiceType(db.Model):
    __tablename__ = 'service_types'

    service_type_id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.String, nullable = True)
    description = db.Column(db.Text)
    base_price = db.Column(db.Float, nullable = False) #set by admin

    services = db.relationship('Service', backref = 'service_type')
    service_professionals = db.relationship('ServiceProfessional', backref = 'service_type')


# 7. Table - activities
class Activity(db.Model):
    __tablename__ = 'activities'

    activity_id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    service_request_id = db.Column(db.Integer, db.ForeignKey('service_request.service_request_id', nullable = False))
    action = db.Column (db.String, nullable = False)
    timestamp = db.Column(db.DateTime, default = datetime.utcnow)
    notes = db.Column(db.Text)

# 8. Table - reviews
class Review(db.Model):
    __tablename__ = 'reviews'

    review_id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    service_request_id = db.Column(db.Integer, db.ForeignKey('service_requests.service_request_id'), nullable = False)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.customer_id'), nullable = False)
    professional_id = db.Column(db.Integer, db.ForeignKey('service_professionals.professional_id'), nullable = False)
    rating = db.Column(db.Integer, nullable = False)
    comments = db.Column(db.Text)
    review_date = db.Column(db.DateTime, default = datetime.utcnow)


# 9. Table = notifications
class Notification(db.Model):
    __tablename__ = 'notifications'

    notification_id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable = False)
    message = db.Column(db.Text, nullable = False)
    is_read = db.Column(db.Boolean, default = False)
    created_at = db.Column(db.DateTime, default = datetime.utcnow)
    notification_type = db.Column(db.String)