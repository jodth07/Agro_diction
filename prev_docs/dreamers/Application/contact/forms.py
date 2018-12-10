from flask_wtf import Form, FlaskForm
from wtforms import StringField, PasswordField, TextAreaField
from wtforms.validators import DataRequired, Length, EqualTo, Email


class MailForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired(), Length(min=3, max=15)])
    last_name = StringField('First Name', validators=[DataRequired(), Length(min=3, max=25)])
    email = StringField('Email', validators=[DataRequired(), Email(), Length(min=6, max=40)])
    title = StringField('Title', validators=[DataRequired(), Length(min=3, max=50)])
    message = TextAreaField('Message', validators=[DataRequired()])
