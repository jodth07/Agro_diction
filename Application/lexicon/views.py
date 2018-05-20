from flask import Blueprint

lexicon_blueprint = Blueprint('lexicon', __name__, template_folder='templates')


@lexicon_blueprint.route('')