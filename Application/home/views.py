from flask import Blueprint

home_blueprint = Blueprint('home', __name__, template_folder='templates')


@home_blueprint.route('/')
def index():
    return 'This is the home page for the dictionary project'
