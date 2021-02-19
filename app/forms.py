
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, Email
from flask_wtf.csrf import CSRFProtect


class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    subject = StringField('Subject', validators=[DataRequired()])
    message = TextAreaField(u'Message', validators=[DataRequired()])
 

#label=('Please enter your full name:') 
#label=('Enter Your e-mail address:'), 
#label=('Please enter the subject of your message:'),
#label=('Please enter the message you would like to send:')