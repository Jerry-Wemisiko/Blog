from typing_extensions import Required
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField, SubmitField,ValidationError
from wtforms.fields.core import BooleanField
from wtforms.validators import Email,Required,EqualTo
from ..models import User

class RegistrationForm(FlaskForm):
    email = StringField('Email Address', validators=[Required(),Email()])
    username = StringField('Username',validators=[Required()])
    password = PasswordField('Password',validators=[Required(),EqualTo('password_confirm',message = 'Password do not match')])
    password_confirm= PasswordField('Confirm Password',validators=[Required()])
    submit = SubmitField('Sign Up')


    def validate_email(self,data_field):
        if User.query.filter_by(email = data_field.data).first():
            raise ValidationError('There is an account with that email')

    def validate_username(self,data_field):
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError('Username is already taken')


class LoginForm(FlaskForm):
    email = StringField('Email Address',validators=[Required(),Email()])    
    password = PasswordField('Password',validators=[Required()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign In')    
