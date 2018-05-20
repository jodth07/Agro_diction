# dreamers/Administration/user/forms.py


from flask_wtf import Form, FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length, EqualTo, Email


class RegisterForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired(), Length(min=3, max=15)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(min=3, max=15)])
    email = StringField('Email', validators=[DataRequired(), Email(), Length(min=6, max=40)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=40)])
    confirm = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email(), Length(min=6, max=40)])
    password = PasswordField('Password', validators=[DataRequired()])


class EmailForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])


class PasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=40)])
    confirm = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])


# to be set later
class UserProfileForm(FlaskForm):
    # id - not changeable
    first_name = StringField('First Name', validators=[DataRequired(), Length(min=3, max=15)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(min=3, max=15)])
    nick_name = StringField('Nick Name', validators=[DataRequired(), Length(min=3, max=15)])
    # show role