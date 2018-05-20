from flask import Blueprint, render_template

article_blueprint = Blueprint('article', __name__, template_folder='templates')


@article_blueprint.route('/article/')
def articles():
    return render_template('articles.html')


@article_blueprint.route('/article/<string:id>')
def article(id):
    return render_template('article.html', id=id)
