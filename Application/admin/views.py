from flask import Blueprint

admin_blueprint = Blueprint('admin', __name__, template_folder='templates')


@admin_blueprint.route('/nimda/')
def amdin():
    return 'This is the admin Page'