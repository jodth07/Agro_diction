from Application import db, bcrypt
from sqlalchemy.ext.hybrid import hybrid_method, hybrid_property
from datetime import datetime
from sqlalchemy.schema import Sequence


def user_role(clearance):
    if int(clearance) == 3000:
        role = 'reviser'
    elif int(clearance) == 5000:
        role = 'publisher'
    elif int(clearance) == 7000:
        role = 'admin'
    else:
        role = 'user'
    return role


def inverse_role(role):
    return {
        'user': int(1000),
        'reviser': int(3000),
        'publisher': int(5000),
        'admin': int(7000)
    }[role]


# 900000
class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, Sequence('users_id_seq', start=1001, increment=1),
                   primary_key=True, autoincrement=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)

    nick_name = db.Column(db.String, nullable=True)
    _has_nick = db.Column(db.Boolean, default=False)

    email = db.Column(db.String, unique=True, nullable=False)
    email_confirmation_sent_date = db.Column(db.DateTime, nullable=True)
    _email_confirmed = db.Column(db.Boolean, nullable=True, default=False)
    email_confirmed_date = db.Column(db.DateTime, nullable=True)

    _password = db.Column(db.Binary(60), nullable=False)
    authenticated = db.Column(db.Boolean, default=False)

    registered_date = db.Column(db.DateTime, nullable=True)
    last_login_date = db.Column(db.DateTime, nullable=True)
    current_login_date = db.Column(db.DateTime, nullable=True)

    # clearance default 1000, levels 1000, 3000, 5000, 7000
    _clearance = db.Column(db.Integer)
    _role = db.Column(db.String, unique=True, nullable=False)
    _cleared = db.Column(db.Boolean, nullable=False)

    # words = db.relationship('Word', backref='user', lazy='dynamic')

    def __init__(self, first_name, last_name, email, plaintext_password, nick_name=None, clearance_level=1000,
                 email_confirmed_date=None):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

        self.email_confirmation_sent_date = datetime.now()
        self.email_confirmed = email_confirmed_date
        self.email_confirmed_date = email_confirmed_date
        # self.email_confirmation = email_confirmed_date

        self.password = plaintext_password
        self.authenticated = False
        self.clearance = clearance_level

        self.registered_date = datetime.now()
        self.last_login_date = None
        self.current_login_date = datetime.now()
        self.nick_name = nick_name
        self.has_nick = nick_name
        self.role = clearance_level

    @hybrid_property
    def email_confirmed(self):
        return self._email_confirmed

    @email_confirmed.setter
    def email_confirmed(self, email_confirmed_date):
        if email_confirmed_date is not None:
            self._email_confirmed = True
        else:
            self._email_confirmed = False
        self.email_confirmed_date = email_confirmed_date

    @hybrid_property
    def has_nick(self):
        return self._has_nick

    @has_nick.setter
    def has_nick(self, nick_name):
        if nick_name is not None:
            self._has_nick = True
        else:
            self._has_nick = False


    @hybrid_property
    def clearance(self):
        return self._clearance

    @clearance.setter
    def clearance(self, clearance_level):
        if clearance_level == 3000:
            self._cleared = True
        elif clearance_level == 5000:
            self._cleared = True
        elif clearance_level == 7000:
            self._cleared = True
        else:
            self._cleared = False
        self._clearance = clearance_level

    @hybrid_property
    def role(self):
        return self._role

    @role.setter
    def role(self, clearance_level):
        self._role = user_role(clearance_level)

    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def password(self, plaintext_password):
        self._password = bcrypt.generate_password_hash(plaintext_password)

    @hybrid_method
    def is_correct_password(self, plaintext_password):
        return bcrypt.check_password_hash(self.password, plaintext_password)

    @property
    def is_authenticated(self):
        """Return True if the user is authenticated."""
        return self.authenticated

    @property
    def is_active(self):
        """Always True, as all users are active."""
        return True

    @property
    def is_anonymous(self):
        """Always False, as anonymous users aren't supported."""
        return False

    def get_id(self):
        """Return the email address to satisfy Flask-Login's requirements."""
        """Requires use of Python 3"""
        return str(self.id)

    def __repr__(self):
        return '<User {0}>'.format(self.name)


# to be added later to set teh auto-increment starting values

