from flask_login import login_required

# from .models import Pitch, User
# from .form import RegistrationForm
from flask import render_template, request, url_for, flash,session
from . import app, db
from werkzeug.security import generate_password_hash, check_password_hash
# from send_email import sender_email


@app.route('/')
def index():

   

    return render_template('index.html')