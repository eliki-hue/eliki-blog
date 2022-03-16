from email.quoprimime import quote
from flask_login import current_user, login_required, login_user, logout_user,logout_user
from datetime import datetime
from .models import Blog, User,Quotes
from .form import RegistrationForm
from flask import render_template, request, url_for, flash,session, Blueprint
from . import  db
from .request import quote_fetch
import urllib.request, json

from sqlalchemy import desc
from werkzeug.security import generate_password_hash, check_password_hash
from send_email import sender_email

views = Blueprint("views", __name__)



@views.route('/')
def index():

    record = Blog.query.all()
   

    quotes=quote_fetch()
    print(quotes)
   

    return render_template('index.html',blogs =record, quotes=quotes )


@views.route("/register")
def register():
    Registration= RegistrationForm()
    

    return render_template('form.html', Registration=RegistrationForm)

@views.route('/success', methods=['GET','POST'])
def success():
    if request.method == "POST":

        username = request.form.get('username')
        email = request.form.get('email')
        password1 = request.form.get('psw1')
        password2 = request.form.get('psw2')
        user_info =db.session.query(User).filter(User.email ==email)
        
        email_exist=User.query.filter_by(email =email).first()
        username_exist = User.query.filter_by(username =username).first()
        if email_exist:
            flash('User with that email address already exist', category='error')
            return render_template('form.html', text ='User with that email address already exist')

        elif username_exist:
            flash('User name already in use', category='error')
            return render_template('form.html', text ='User name already in use.')

        elif password1 != password2 :
            flash( 'Password dont\'t match' , category='error')
            return render_template('form.html', text ='Password don\'t match!')

        elif len(password1) < 6:
            flash('Password is too short', category='error')
            return render_template('form.html', text ='password too short. use at least 6 characters')

        else:
            data = User(username,email,password=generate_password_hash(password1, method='sha256'))

            db.session.add(data)
            db.session.commit()
            # logout_user(data)
            try:
                sender_email(email, username)
            except:
                pass
            
            return render_template('success.html')
    
       


@views.route('/login' )
def login():
    return render_template('login.html')


@views.route('/profile', methods=['GET','POST'])
def profile():
    if request.method == "POST":

       
        email = request.form.get('email')
        password = request.form.get('psw')

        user = User.query.filter_by(email=email).first()
        if not user or not check_password_hash(user.password, password):
            text='Please check your login details and try again.'
            return render_template('login.html', text=text)
        session['email']=user.email
        name = user.username
        
        
        # login_user(user, remember= True)
        return render_template('profile.html',user=user)


            
@views.route('/blogForm')
def blogForm():

    return render_template('blogForm.html')

@views.route('/blog',methods=['GET','POST'])
def blog():
     
     if request.method == "POST":
         
        
         category = request.form.get('category')
         username = request.form.get('username')
         title = request.form.get('title')
         image =request.form.get('image_url')
         blog = request.form.get('blog')
         link = request.form.get('link')
         date = datetime.today().strftime('%Y-%m-%d')
         
        
         if image:
             image_url=image
         else:
             image_url='no image'

         
         data = Blog(category,username,title,image_url,blog,link,date)
         db.session.add(data)
         print(data)
         db.session.commit()
         print(date)

     return render_template('blogsuccess.html')

@views.route('/display')
def display():
    record = Blog.query.all()

    return render_template('index.html',blogs =record)

@views.route('/blogsuccess')
def blogsuccess():
    return render_template('blogsuccess.html')


# @views.route('/logout')
# @login_required
# def logout():
#     logout_user(current_user.id)
#     return render_template(url_for(views.index))
