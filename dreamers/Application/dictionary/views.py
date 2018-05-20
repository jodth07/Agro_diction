from flask import Blueprint, flash, render_template, request, redirect, url_for
from sqlalchemy.exc import IntegrityError

from Application import db
from .models import *
from .forms import WordForm, PART_OF_SPEECH


dict_blueprint = Blueprint('dictionary', __name__, template_folder='templates')


@dict_blueprint.route('/words/')
def words():
    all_words = Dictionary.query.all()
    return render_template("words.html", words=all_words)


@dict_blueprint.route('/words/<word_id>')
def view_word(word_id):
    word = Dictionary.query.get(word_id)
    return render_template('word.html', word=word)


@dict_blueprint.route('/user/add', methods=['GET', 'POST'])
def add_word():
    form = WordForm(request.form)
    form.category.choices = [(key, value) for key, value in PART_OF_SPEECH]
    if request.method == 'GET':
        return render_template('add_word.html', form=form)
    if request.method == 'POST':
        if form.validate_on_submit():
            try:
                new_word = Word(form.common_name.data, form.category.data)
                db.session.add(new_word)
                db.session.commit()
                flash('Thanks for registering!', 'success')
                return redirect(url_for('dictionary.words'))
            except IntegrityError:
                db.session.rollback()
                flash('ERROR! word ({}) already exists.'.format(form.common_name.data), 'error')
    return render_template('add_word.html', form=form)
