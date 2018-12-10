from flask import Blueprint, render_template, request, redirect
from .models import Article
from .forms import SearchForm

article_blueprint = Blueprint('article', __name__, template_folder='templates')


@article_blueprint.route('/article/')
def view_articles():
    form = SearchForm(request.form)
    all_words = Article.query.limit(10)
    n = 0;
    article_set_1 = []
    article_set_2 = []
    for word in all_words:
        n += 1;
        if n <= 5:
            article_set_1.append(word)
        else:
            article_set_2.append(word)
    return render_template('view_articles.html', form=form, article_set_1=article_set_1, article_set_2=article_set_2)


@article_blueprint.route('/article/<string:id>')
def view_article(id):
    article = Article.query.get(id=id)
    return render_template('view_article.html', article=article)
