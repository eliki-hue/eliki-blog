

from sqlalchemy import func

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
    author = db.Column(db.String(255))
    title = db.Column(db.String(255))
    image_url = db.Column(db.String(255))
    blog =db.Column(db.String(10000))
    link =db.Column(db.String(255))    
    published_at = db.Column(db.DateTime(timezone=True), default = func.now())
    

    def __init__(self, category, author, title, image_url,blog,link,published_at):
        self.category = category        
        self.author = author         
        self.title = title
        self.image_url = image_url
        self.blog = blog
        self.published_at =published_at
        self.link= link
       


    def __repr__(self):
        return f'User {self.author}'


class Quotes:

    def __init__(self, author, quote):

        self.author = author

        self.quote = quote 

    def __repr__(self):
        return f'Quote {self.author}'