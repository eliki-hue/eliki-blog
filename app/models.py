from unicodedata import category
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime



class User(UserMixin,db.Model):
    '''
    class that handles the user infomation
    '''
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    password= db.Column(db.String(255))
    pitches = db.relationship('Pitch', backref = 'user', lazy = 'dynamic')

    def __init__(self, username,email,password):
        self.username= username
        self.email=email
        self.password=password 