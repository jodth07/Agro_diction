import json
from datetime import datetime
from sqlalchemy.schema import Sequence
from sqlalchemy.ext.hybrid import hybrid_property

from Application import db


class Blog(db.Model):
    """
    Blog model for database table blogs
    """

    __tablename__= "blogs"

    id = db.Column(db.Integer, Sequence('dictionary_id_seq', start=100001, increment=1), primary_key=True)
    title = db.Column(db.String, nullable=False)
    author = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)
    category = db.Column(db.String, nullable=False)
    short_description = db.Column(db.String, nullable=False)

    is_defined = db.Column(db.Boolean, default=False)
    define_date = db.Column(db.DateTime, nullable=False)
    definer_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    # definer = db.relationship('User', backref=db.backref('defined_word', lazy='dynamic'), foreign_keys=[definer_id])

    is_revised = db.Column(db.Boolean, default=False)
    revised_date = db.Column(db.DateTime, nullable=True)
    reviser_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    # revise = db.relationship('User', backref=db.backref('revised_word', lazy='dynamic'), foreign_keys=[reviser_id])

    is_published = db.Column(db.Boolean, default=False)
    published_date = db.Column(db.DateTime, nullable=True)
    publisher_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    # publisher = db.relationship('User', backref=db.backref('published', lazy='dynamic'), foreign_keys=[publisher_id])

    _tags = db.Column(db.String, nullable=True)
    source = db.Column(db.String)
    views = db.Column(db.Integer)
    searched = db.Column(db.Integer)

    description = db.Column(db.String, nullable=False)
    scientific_name = db.Column(db.String, nullable=False)
    visibility = db.Column(db.String, nullable=False)

    def __init__(self, title, category, author, short_description, defined_user_id=0, tag=[], visible='Private',
                 source="",  description=[]):
        self.sg_tags = tag
        self.author = author
        self.title = title
        self.name = title
        self.category = category
        self.short_description = short_description

        self.source = source
        self.views = 0
        self.searched = 0

        self.visibility = visible
        self.sg_description = description

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
    def sg_description(self):
        return json.loads(self.description)

    @sg_description.setter
    def sg_description(self, description):
        self.description = json.dumps(description)