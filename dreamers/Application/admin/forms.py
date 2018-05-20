from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, FieldList, TextAreaField
from wtforms.validators import DataRequired, Length, EqualTo, Email


# Tuple list of words' classes
PART_OF_SPEECH = [
    ('Noun', 'Noun'),
    ('Determiner', 'Determiner'),  # article
    ('Pronoun', 'Pronoun'),
    ('Verb', 'Verb'),
    ('Adjective', 'Adjective'),
    ('Adverb', 'Adverb'),
    ('Conjunction', 'Conjunction'),
    ('Interjection', 'Interjection')
]

# Subtype of Nouns Based on Agro classification
SUB_NOUNS = [
    ('None', 'none'),
    ('Animals', 'animals'),
    ('Plants', 'plants'),
    ('Tools', 'tools')
]

VISIBILITY = [
    ('Private', 'Private'),
    ('Public', 'Public')
]

STATUS = [
    ('Added', 'Added'),
    ('Revised', 'Revised'),
    ('Published', 'Published')
]


class DictionaryAddForm(FlaskForm):
    common_name = StringField('Common Name', validators=[DataRequired(), Length(min=3, max=15)])
    category = SelectField('Category', validators=[DataRequired()], choices=PART_OF_SPEECH)
    short_description = TextAreaField('Short Description', validators=[DataRequired(), Length(min=10, max=250)])
    tags = FieldList(StringField('Tags'), min_entries=2, max_entries=7)

    sub_category = SelectField('Sub-Category', validators=[DataRequired()], choices=SUB_NOUNS)

    other_names = FieldList(StringField('Other Names'), min_entries=1, max_entries=7)
    definitions = FieldList(TextAreaField('Definitions'), min_entries=1, max_entries=7)
    examples = FieldList(TextAreaField('Examples'), min_entries=1, max_entries=7)
    synonyms = FieldList(TextAreaField('Synonyms'), min_entries=1, max_entries=7)
    antonyms = FieldList(TextAreaField('Antonyms'), min_entries=1, max_entries=7)
    descriptions = FieldList(TextAreaField('Descriptions'), min_entries=1, max_entries=7)

    other_info = FieldList(TextAreaField('Other Info'), min_entries=1, max_entries=7)
    source = StringField('Source', validators=[DataRequired()])
    visibility = SelectField('Category', validators=[DataRequired()], choices=VISIBILITY)

    scientific_name = StringField('scientific_name', validators=[DataRequired()])
    family = StringField('family', validators=[DataRequired()])


class DictionaryUpdateForm(FlaskForm):
    common_name = StringField('Common Name', validators=[DataRequired(), Length(min=3, max=15)])
    category = SelectField('Category', validators=[DataRequired()], choices=PART_OF_SPEECH)
    short_description = TextAreaField('Short Description', validators=[DataRequired(), Length(min=10, max=250)])
    tags = FieldList(StringField('Tags'), min_entries=2, max_entries=7)
    noun_type = SelectField('Sub-Category', validators=[DataRequired()])
    other_names = FieldList(StringField('Other Names'), min_entries=1, max_entries=7)
    definitions = FieldList(TextAreaField('Definitions'), min_entries=1, max_entries=7)
    examples = FieldList(TextAreaField('Examples'), min_entries=1, max_entries=7)
    synonyms = FieldList(TextAreaField('Synonyms'), min_entries=1, max_entries=7)
    antonyms = FieldList(TextAreaField('Antonyms'), min_entries=1, max_entries=7)
    other_info = FieldList(TextAreaField('Other Info'), min_entries=1, max_entries=7)
    source = StringField('Source', validators=[DataRequired()])
    scientific_name = StringField('scientific_name', validators=[DataRequired()])
    family = StringField('family', validators=[DataRequired()])
    status = SelectField('Category', validators=[DataRequired()], choices=STATUS)

