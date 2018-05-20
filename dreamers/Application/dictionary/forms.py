from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms.validators import DataRequired, Length

# Tuple list of words' classes
PART_OF_SPEECH = [
    ('Noun', 'noun'),
    ('Determiner', 'determiner'),  # article
    ('Pronoun', 'Pronoun'),
    ('Verb', 'verb'),
    ('Adjective', 'adjective'),
    ('Adverb', 'adverb'),
    ('Conjunction', 'conjunction'),
    ('Interjection', 'interjection')
]


# Subtype of Nouns Based on Agro classification
SUB_NOUNS = [
    ('Animals', 'animals'),
    ('Plants', 'plants'),
    ('Tools', 'tools')
]


class WordForm(FlaskForm):
    common_name = StringField('Common Name', validators=[DataRequired(), Length(min=3, max=15)])
    category = SelectField('Category', validators=[DataRequired()], id='select_category')


class NounForm(FlaskForm):
    pass


class DeterminerForm(FlaskForm):
    pass


class PronounForm(FlaskForm):
    pass


class VerbForm(FlaskForm):
    pass


class AdjectiveForm(FlaskForm):
    pass


class AdverbForm(FlaskForm):
    pass


class ConjunctionForm(FlaskForm):
    pass


class InterjectionForm(FlaskForm):
    pass


class PlantForm(FlaskForm):
    pass


class AnimalForm(FlaskForm):
    pass

