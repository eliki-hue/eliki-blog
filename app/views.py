from flask_login import login_required

from .models import Pitch, User
from .form import RegistrationForm
from flask import render_template, request, url_for, flash,session, Blueprint
from . import  db
from werkzeug.security import generate_password_hash, check_password_hash
from send_email import sender_email

views = Blueprint("views", __name__)

# app = create_app()

@views.route('/')
def index():

    record = Pitch.query.all()

    return render_template('index.html',pitches =record)


@views.route("/register")
def register():
    Registration= RegistrationForm()
    

    return render_template('form.html', Registration=RegistrationForm)

@views.route('/success', methods=['GET','POST'])
def success():
    if request.method == "POST":

        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('psw')
        if db.session.query(User).filter(User.email ==email).count()==0:

            print(username)
            print(email)
            print(password)
            data = User(username,email,password=generate_password_hash(password, method='sha256'))

            db.session.add(data)
            db.session.commit()
            try:
                sender_email(email, username)
            except:
                pass
            
            return render_template('success.html')
    
        return render_template('form.html', text ='User with that email address already exist')


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
        mypitch= Pitch.query.filter_by(sender=name)  
        return render_template('profile.html',user=user, mypitch=mypitch)


            
@views.route('/pitchForm')
def pitchForm():

    return render_template('pitchForm.html')

@views.route('/pitch',methods=['GET','POST'])
def pitch():
     
     if request.method == "POST":
         
         sender = request.form.get('sender')
         category = request.form.get('category')
         pitch = request.form.get('pitch')
         
         data = Pitch(category, pitch, sender,1,0,0,'great')
         db.session.add(data)
         print(data)
         db.session.commit()

     return render_template('pitchsuccess.html')

@views.route('/display')
def display():
    record = Pitch.query.all()

    return render_template('index.html',pitches =record)

@views.route('/pitchsuccess')
def pitchsuccess():
    return render_template('pitchsuccess.html')




