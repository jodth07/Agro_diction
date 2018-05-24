import json
from sqlalchemy.exc import IntegrityError
from flask_login import login_user, current_user, login_required, logout_user
from flask import Blueprint, render_template, redirect, url_for, abort, request, flash

from .forms import *
from Application import db
from Application.user.models import User
from Application.dictionary.models import Dictionary

admin_blueprint = Blueprint('admin', __name__, template_folder='templates', url_prefix='/novis_ta')


# ==================================================== #
#       ADMIN: VIEW HOME STATS                         #
# ==================================================== #
@admin_blueprint.route('/')
@login_required
def admin_home():
    if current_user._role == 'user':
        return redirect(url_for('home.index'))
    else:
        return render_template('admin_home.html')


# ==================================================== #
#       ADMIN: VIEW ARTICLES STATS AND CRUD               #
# ==================================================== #
@admin_blueprint.route('/articles/')
@login_required
def view_articles():
    return render_template("article/view_articles.html")


@admin_blueprint.route('/article/<article>')
@login_required
def article(article):
    return render_template("article/view_article.html")


# ==================================================== #
#       ADMIN: VIEW BLOGS STATS AND CRUD               #
# ==================================================== #
@admin_blueprint.route('/blogs/')
@login_required
def view_blogs():
    return render_template('blog/view_blogs.html')


@admin_blueprint.route('/blog/<blog>')
@login_required
def blog(blog):
    return "blog crud {}".format(blog)


# ==================================================== #
#       ADMIN: VIEW WORDS STATS AND CRUD               #
# ==================================================== #


@admin_blueprint.route('/words')
@login_required
def view_words():
    words = Dictionary.query.all()
    return render_template('dictionary/view_words.html', words=words)


# sg -> setter and getter
@admin_blueprint.route('/word/<word_id>')
@login_required
def view_word(word_id):

    word = Dictionary.query.filter_by(id=word_id).first()
    # if word.sg_tags:
    #     tags = json.loads(word.sg_tags)

    return render_template('dictionary/view_word.html', word=word)


@admin_blueprint.route('/addword/', methods=['GET', 'POST'])
@login_required
def create_entry():
    current_user_id = current_user.id

    form = DictionaryAddForm(request.form)
    if request.method == 'GET':
        return render_template('dictionary/create_entry.html', form=form)
    if request.method == 'POST':
        if form.validate_on_submit():
            try:
                new_word = Dictionary(form.common_name.data, form.category.data, form.short_description.data,
                                      current_user_id)
                new_word.sg_tags = form.tags.data

                new_word.sg_other_names = form.other_names.data
                new_word.sg_definitions = form.definitions.data
                new_word.sg_examples = form.examples.data
                new_word.sg_synonyms = form.synonyms.data
                new_word.sg_antonyms = form.antonyms.data
                new_word.sg_other_info = form.other_info.data
                new_word.source = form.source.data

                new_word.visibility = form.visibility.data
                new_word.sub_category = form.sub_category.data
                new_word.sg_definitions = form.descriptions.data
                new_word.sg_scientific_name = form.scientific_name.data
                new_word.family = form.family.data

                new_word.defined_user_id = current_user.id

                db.session.add(new_word)
                db.session.commit()

                word = Dictionary.query.filter_by(id=new_word.id).first()
                word_id = word.id
                flash('Thanks for registering word {}!'.format(word_id), 'success')
                return redirect(url_for('admin.admin_home'))
            except IntegrityError:
                db.session.rollback()
                flash('ERROR! word ({}) already exists.'.format(form.common_name.data), 'error')
    return render_template('dictionary/create_entry.html', form=form)


@admin_blueprint.route('/editword/<word_id>', methods=['GET', 'POST'])
@login_required
def update_entry(word_id):
    word = Dictionary.query.get(word_id)
    form = DictionaryUpdateForm(request.form)

    if request.method == 'GET':
        flash('completing word {}'.format(word.id), 'success')
        return render_template('dictionary/update_entry.html', form=form, word=word)
    if request.method == 'POST':

        if form.validate_on_submit():
            try:

                word.common_name = form.common_name.data
                word.category = form.category.data
                word.short_description = form.short_description.data

                word.sg_tags = form.tags.data

                word.sg_other_names = form.other_names.data
                word.sg_definitions = form.definitions.data
                word.sg_examples = form.examples.data
                word.sg_synonyms = form.synonyms.data
                word.sg_antonyms = form.antonyms.data
                word.sg_other_info = form.other_info.data
                word.source = form.source.data

                word.visibility = form.visibility.data
                word.sub_category = form.sub_category.data
                word.sg_definitions = form.descriptions.data
                word.sg_scientific_name = form.scientific_name.data
                word.family = form.family.data

                word.revised_user_id = current_user.id

                # db.session.add(new_word)
                db.session.commit()
                flash('new word {} added to dictionary'.format(word.common_name), 'success')
                return redirect(url_for('admin.view_words'))
            except IntegrityError:
                db.session.rollback()
                flash('ERROR! word ({}) already exists.'.format(form.common_name.data), 'error')
    return render_template('dictionary/update_entry.html', form=form)


# ==================================================== #
#           ADMIN: VIEW CONTACTS                       #
# ==================================================== #
@admin_blueprint.route('/contact')
@login_required
def contact_us():
    return "contact_us crud "


# ==================================================== #
#           ADMIN: VIEW USERS STATS                    #
# ==================================================== #
@admin_blueprint.route('/view_users/')
@login_required
def admin_view_users():
    if current_user.clearance != 7000:
        abort(403)
    else:
        users = User.query.order_by(User.id).all()
        return render_template('user/view_users.html', users=users)
    return redirect(url_for('home.index'))  # Not sure what this means

