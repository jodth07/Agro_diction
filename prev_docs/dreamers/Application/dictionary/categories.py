from .. import db


class Word(db.Model):

    __tablename__= "words"

    id = db.Column(db.Integer, primary_key=True)
    common_name = db.Column(db.String, nullable=False)
    category = db.Column(db.String, nullable=False)
    other_names = db.Column(db.String)
    definitions = db.Column(db.String)
    examples = db.Column(db.String)
    synonyms = db.Column(db.String, nullable=True)
    antonyms = db.Column(db.String, nullable=True)
    other_info = db.Column(db.String, nullable=True)
    source = db.Column(db.String)

    def __init__(self, common_name, category, other_names=[], definitions=[],
                 examples=[], synonyms=[], antonyms=[], other_info=[], source = ""):
        self.common_name = common_name
        self.category = category
        self.other_names = other_names
        self.definitions = definitions
        self.examples = examples
        self.synonyms = synonyms
        self.antonyms = antonyms
        self.other_info = other_info
        self.source = source

    def __repr__(self):
        return "Common name: {}, category: {}".format(self.common_name, self.category)


class Noun(db.Model):

    __tablename__ ="nouns"

    id = db.Column(db.Integer, primary_key=True)
    common_name = db.Column(db.String, nullable=False)
    category = db.Column(db.String, nullable=False)
    other_names = db.Column(db.String)
    definitions = db.Column(db.String)
    examples = db.Column(db.String)
    synonyms = db.Column(db.String, nullable=True)
    antonyms = db.Column(db.String, nullable=True)
    other_info = db.Column(db.String, nullable=True)
    source = db.Column(db.String)
    tag = db.Column(db.String)

    def __init__(self, common_name, category, other_names=[], definitions=[],
                 examples=[], synonyms=[], antonyms=[], other_info=[], source = ""):
        self.common_name = common_name
        self.category = category
        self.other_names = other_names
        self.definitions = definitions
        self.examples = examples
        self.synonyms = synonyms
        self.antonyms = antonyms
        self.other_info = other_info
        self.source = source


class Determiner(Word):

    __tablename__ = "determiners"

    def __init__(self):
        self.category = "Determiner"


class Pronoun(db.Model):

    __tablename__ = "pronouns"

    def __init__(self):
        self.category = "Pronoun"


class Verb(db.Model):

    __tablename__ = "verbs"

    def __init__(self):
        self.category = "Verb"


class Adverb(db.Model):

    __tablename__ = "adverbs"

    def __init__(self):
        self.category = "Adverb"


class Adjective(db.Model):

    __tablename__ = "adjectives"

    def __init__(self):
        self.category = "Adjective"
        self.common_name = ""


class Preposition(db.Model):

    __tablename__ = "prepositions"

    def __init__(self):
        self.category = "Preposition"


class Conjunction(db.Model):

    __tablename__ = "conjunctions"

    def __init__(self):
        self.category = "Conjunction"


class Interjection(db.Model):

    __tablename__ = "interjections"

    def __init__(self):
        self.category = "Interjection"
        self.common_name = ""


class Plant(db.Model):

    __tablename__ = "plants"

    def __init__(self, scientific_name="", family="", description = []):
        self.tag = "Plant"
        self.category = "Noun"
        self.scientific_name = scientific_name
        self.family = family
        self.description = description

    def __repr__(self):

        return "Common Name: {}\n tag: {}\n category: {}.".format(self.common_name, self.tag, self.category)


class Animal(db.Model):

    __tablename__ = "animals"

    def __init__(self, scientific_name="", family="", description=[]):
        self.tag = "Animal"
        self.category = "Noun"
        self.scientific_name = scientific_name
        self.family = family
        self.description = description

    def __repr__(self):
        return "Common Name: {}\n tag: {}\n category: {}".format(self.common_name, self.tag, self.category)


class Tool(db.Model):

    __tablename__ = "tools"

    def __init__(self, description):
        self.tag = "Tool"
        self.category = "Noun"
        self.description = description

