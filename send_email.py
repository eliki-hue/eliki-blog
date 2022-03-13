import imp
from flask_mail import Message
from flask import render_template
from email.mime.text import MIMEText
import smtplib

# def mail_message(username):
#     sender_email = 'eliki13720@gmail.com'
#     subject= 'Welcome to pitch_test'
#     email = Message(subject=subject, sender=sender_email, recipients=username)
#     email.body = '''
#     Hello {{username}},
#     We have noticed that you have registered to pitch_test. Welcome and have fun creating your 1 minute pitch and seeing other peoples pitch_test

#     '''
   
#     mail.send(email)
def sender_email(email,username):
    from_email ='eliki13720@gmail.com'
    from_password = 'eliki30808983%'
    to_email =email

    subject = 'Welcome to Pitch_test'
    message ='Hello {username} we noticed that you have registered to our website. Enjoy!'

    msg =MIMEText(message, 'html')
    msg['Subject'] =subject
    msg['To'] = to_email
    msg['FROM'] = from_email

    gmail =smtplib.SMTP('smpt.gmail.com', 465)
    gmail.ehlo
    gmail.starttlsz
    gmail.login(from_email, from_password)
    gmail.send_message(msg)
    return 'email sent'