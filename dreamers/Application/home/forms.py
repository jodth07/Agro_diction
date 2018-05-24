from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, FieldList, TextAreaField
from wtforms.validators import DataRequired, Length, EqualTo, Email


class SearchForm(FlaskForm):
    query_text = StringField('search', validators=[DataRequired(False), Length(min=2)])
    # sort_ascending =
    # query_animals =
    # query_plants =
    # query_tools =
