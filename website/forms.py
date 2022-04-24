from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import (
    DataRequired,
    Length,
)

class SignupForm(FlaskForm):
    """User signup form"""

    name = StringField(
        'Name',
        validators=[DataRequired()]
    )
    username = StringField(
        'Username',
        validators=[
            Length(min=3, message='Minimum length 3 characters'),
            DataRequired()
        ]
    )
    password = StringField(
        'Password',
        validators=[
            DataRequired(),
            Length(min=6, message='Select a stronger password')
        ]
    )
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    """User login form"""
    username = StringField(
        'Username',
        validators=[
            DataRequired()
        ]
    )
    password = PasswordField(
        'Password',
        validators=[DataRequired()]
    )
    submit = SubmitField('Login')