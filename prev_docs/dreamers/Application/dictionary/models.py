import json
from datetime import datetime
from sqlalchemy.schema import Sequence
from sqlalchemy.ext.hybrid import hybrid_property, hybrid_method

from Application import db


class Dictionary(db.Model):

    __tablename__= "dictionary"

    id = db.Column(db.Integer, Sequence('dictionary_id_seq', start=100001, increment=1), primary_key=True)
    common_name = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)
    origin = db.Column(db.String, nullable=True)
    category = db.Column(db.String, nullable=False)
    short_description = db.Column(db.String, nullable=False)

    is_defined = db.Column(db.Boolean, default=False)
    define_date = db.Column(db.DateTime, nullable=False)
    definer_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    definer = db.relationship('User', backref=db.backref('defined_word', lazy='dynamic'), foreign_keys=[definer_id])

    is_revised = db.Column(db.Boolean, default=False)
    revised_date = db.Column(db.DateTime, nullable=True)
    reviser_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    revise = db.relationship('User', backref=db.backref('revised_word', lazy='dynamic'), foreign_keys=[reviser_id])

    is_published = db.Column(db.Boolean, default=False)
    published_date = db.Column(db.DateTime, nullable=True)
    publisher_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    publisher = db.relationship('User', backref=db.backref('published', lazy='dynamic'), foreign_keys=[publisher_id])

    _tags = db.Column(db.String, nullable=True)
    other_names = db.Column(db.String)
    definitions = db.Column(db.String)
    examples = db.Column(db.String)
    synonyms = db.Column(db.String, nullable=True)
    antonyms = db.Column(db.String, nullable=True)
    other_info = db.Column(db.String, nullable=True)
    source = db.Column(db.String)
    views = db.Column(db.Integer)
    searched = db.Column(db.Integer)

    sub_category = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    scientific_name = db.Column(db.String, nullable=False)
    family = db.Column(db.String, nullable=False)
    visibility = db.Column(db.String, nullable=False)

    def __init__(self, common_name, category, short_description, defined_user_id=0, tag=[], other_names=[],
                 definitions=[], visible='Private', examples=[], synonyms=[], antonyms=[], other_info=[], source="",
                 scientific_name=[], sub_category="", description=[], family=''):
        self.sg_tags = tag
        self.common_name = common_name
        self.name = common_name
        self.category = category
        self.short_description = short_description

        self.sg_other_names = other_names
        self.sg_definitions = definitions
        self.sg_examples = examples
        self.sg_synonyms = synonyms
        self.sg_antonyms = antonyms
        self.sg_other_info = other_info
        self.source = source
        self.views = 0
        self.searched = 0

        self.visibility = visible
        self.sub_category = sub_category
        self.sg_description = description
        self.sg_scientific_name = scientific_name
        self.family = family

        self.is_defined = False
        self.define_date = datetime.now()
        self.defined_user_id = defined_user_id

        self.is_revised = False
        self.revised_date = None
        self.revised_user_id = None
        #
        self.is_published = False
        self.published_date = None
        self.published_user_id = None

    def __repr__(self):
        return '<title {}'.format(self.name)

    def get_id(self):
        return self.id

    @hybrid_property
    def sg_tags(self):
        return json.loads(self._tags)

    @sg_tags.setter
    def sg_tags(self, tags_list):
        self._tags = json.dumps(tags_list)

    @hybrid_property
    def sg_other_names(self):
        return json.loads(self.other_names)

    @sg_other_names.setter
    def sg_other_names(self, other_names):
        self.other_names = json.dumps(other_names)

    @hybrid_property
    def sg_definitions(self):
        return json.loads(self.definitions)

    @sg_definitions.setter
    def sg_definitions(self, definitions_list):
        self.definitions = json.dumps(definitions_list)

    @hybrid_property
    def sg_examples(self):
        return json.loads(self.examples)

    @sg_examples.setter
    def sg_examples(self, examples_list):
        self.examples = json.dumps(examples_list)

    @hybrid_property
    def sg_synonyms(self):
        return json.loads(self.synonyms)

    @sg_synonyms.setter
    def sg_synonyms(self, syns_list):
        self.synonyms = json.dumps(syns_list)

    @hybrid_property
    def sg_antonyms(self):
        return json.loads(self.antonyms)

    @sg_antonyms.setter
    def sg_antonyms(self, ants_list):
        self.antonyms = json.dumps(ants_list)

    @hybrid_property
    def sg_other_info(self):
        return json.loads(self.other_info)

    @sg_other_info.setter
    def sg_other_info(self, lister):
        self.other_info = json.dumps(lister)

    @hybrid_property
    def sg_scientific_name(self):
        return json.loads(self.scientific_name)

    @sg_scientific_name.setter
    def sg_scientific_name(self, lister):
        self.scientific_name = json.dumps(lister)

    @hybrid_property
    def sg_description(self):
        return json.loads(self.description)

    @sg_description.setter
    def sg_description(self, description):
        self.description = json.dumps(description)

