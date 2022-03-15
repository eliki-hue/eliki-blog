from unicodedata import category
from pytz import timezone

from sqlalchemy import func

from app.views import blog
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
    blog =db.relationship('Blog', backref= 'user', passive_deletes =True)
    # blogs = db.relationship('Blog', backref = 'user', lazy = 'dynamic')

    def __init__(self, username,email,password):
        self.username= username
        self.email=email
        self.password=password 

    # @property
    # def password(self):
    #     raise AttributeError('You cannot read the password attribute')

    # @password.setter
    # def password(self, password):
    #     self.pass_secure = generate_password_hash(password)

    # def verify_password(self,password):
    #     return check_password_hash(self.pass_secure,password)

    # from . import login_manager

    # @login_manager.user_loader
    # def load_user(user_id):
    #     return User.query.get(int(user_id))

    def __repr__(self):
        return f'User {self.username}'

class Blog(db.Model):
    __tablename__ = 'blogs'

    id = db.Column(db.Integer, primary_key= True)
    category =db.Column(db.String(255))
    blog =db.Column(db.String())
    upvote = db.Column(db.Integer)
    downvote = db.Column(db.Integer)
    author = db.Column(db.Integer,db.ForeignKey('user.id', ondelete='CASCADE'), nullability=False)
    comments = db.Column(db.String)
    published_at = db.Column(db.DateTime(timezone=True), default = func.now())
    

    def __init__(self, category, blog, upvote, downvote,sender,comments,published_at):
        self.category = category        
        self.blog = blog         
        self.upvote = upvote
        self.downvote = downvote
        self.comments = comments
        self.published_at =published_at
        self.sender=sender
       


    def __repr__(self):
        return f'User {self.sender}'