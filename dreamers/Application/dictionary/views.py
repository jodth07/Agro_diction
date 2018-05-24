from flask import Blueprint, render_template, request

# Local Imports
from .models import Dictionary
from .forms import SearchForm


dict_blueprint = Blueprint('dictionary', __name__, template_folder='templates')


@dict_blueprint.route('/words')
def words():
    form = SearchForm(request.form)
    all_words = Dictionary.query.limit(10)
    n = 0;
    words_set_1 = []
    words_set_2 = []
    for word in all_words:
        n += 1;
        if n <= 5:
            words_set_1.append(word)
        else:
            words_set_2.append(word)

    return render_template("words.html", words=all_words, form=form, words_set_1=words_set_1, words_set_2=words_set_2)


@dict_blueprint.route('/words/<word_id>')
def view_word(word_id):
    word = Dictionary.query.get(word_id)
    return render_template('word.html', word=word)


# @dict_blueprint.route('/search', methods=['GET', 'POST'])
# def search():
#     form = SearchForm(request.form)
#     boy=['string one', 'string two']
#
#     if request.method == 'GET':
#         return render_template('includes/search.html', form=form, boy=boy)
#     if request.method == 'POST':
#         if form.validate_on_submit():
#             qry_data = form.query_text.data
#             return search_results(qry_data)
#
#     return render_template('includes/search.html', form=form, boy=boy)


@dict_blueprint.route('/words/results')
def search_results(qry):

    return render_template('search_results.html')