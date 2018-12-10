from flask import Blueprint, render_template, request, redirect, url_for
from .forms import SearchForm
from Application.dictionary.models import Dictionary

home_blueprint = Blueprint('home', __name__, template_folder='templates')


@home_blueprint.route("/", methods=['GET', 'POST'])
def index():
    form = SearchForm(request.form)
    if request.method == 'GET':
        # return render_template('search.html', form=form)
        return render_template('index.html', form=form)
    if request.method == 'POST':
        if form.validate_on_submit():
            # qry_data = form.query_text.data
            qry_data = request.form.get("query_text", "")
            print(qry_data)

            # return redirect(url_for('home.search_results', qry_data = form.query_text.data ))
            return search_results(qry_data)
    # return render_template('search.html', form=form)
    return render_template('index.html', form=form)


@home_blueprint.route('/')
def search():
    pass


@home_blueprint.route('/results/<qry_data>')
def search_results(qry_data):
    count = 0
    results = Dictionary.query.filter_by(name=qry_data)
    if results:
        print("True")
        print(type(results))
        for result in results:
            count += 1
            print(count)

    return render_template('includes/search_results.html', results=results, searched=qry_data, count=count)
