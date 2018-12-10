from flask import Blueprint, request, flash, redirect, url_for, render_template, abort
from sqlalchemy.exc import IntegrityError
from flask_login import login_user, current_user, login_required, logout_user
from flask_mail import Message
from threading import Thread
from itsdangerous import URLSafeTimedSerializer
from datetime import datetime

# Local Imports
from Application import db, mail, app
from .forms import RegisterForm, LoginForm, EmailForm, PasswordForm, UserProfileForm
from .models import User

user_blueprint = Blueprint('user', __name__, template_folder='templates')


# ==================================================== #
# REUSABLE EMAILING METHODS                            #
# ==================================================== #
def send_async_mail(msg):
    with app.app_context():
        mail.send(msg)


def send_email(subject, recipients, html_body, text_body=None):
    msg = Message(subject, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    msg.add_recipient('olsonpho@gmail.com')
    # mail.send(msg)
    thr = Thread(target=send_async_mail, args=[msg])
    thr.start()


# ==================================================== #
# CREATING USER REGISTRATION AND CONFIRMATION OF EMAIL #
# ==================================================== #
@user_blueprint.route('/register/', methods=['GET', 'POST'])
def user_registration():
    form = RegisterForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            try:
                new_user = User(form.first_name.data, form.last_name.data, form.email.data, form.password.data)
                new_user.authenticated = True
                db.session.add(new_user)
                db.session.commit()
                login_user(new_user)
                send_confirmation_email(new_user.email, new_user.last_name)
                flash('Thanks for registering! A link has been sent to your email for confirmation', 'success')
                return redirect(url_for('user.login'))
            except IntegrityError:
                db.session.rollback()
                flash('ERROR! Email ({}) already exists.'.format(form.email.data), 'error')
    return render_template('register.html', form=form)


def send_confirmation_email(user_email, user_name):
    confirm_serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])

    confirm_url = url_for(
        'user.confirm_email',
        token=confirm_serializer.dumps(user_email,
                                       salt='email-confirmation-salt'),
        _external=True)

    html = render_template(
        'email_confirmation.html',
        confirm_url=confirm_url, user_name=user_name)

    send_email('Confirm Your Email Address', [user_email], html)


@user_blueprint.route('/confirm/<token>')
def confirm_email(token):
    try:
        confirm_serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])
        email = confirm_serializer.loads(token, salt='email-confirmation-salt', max_age=3600)
    except:
        flash('The confirmation link is invalid or has expired.', 'error')
        return redirect(url_for('user.user_registration'))

    user = User.query.filter_by(email=email).first()

    if user.email_confirmed:
        flash('Account already confirmed. Please login.', 'info')
    else:
        user.email_confirmed = True
        user.email_confirmed_date = datetime.now()
        db.session.add(user)
        db.session.commit()
        flash('Thank you for confirming your email address!')

    return redirect(url_for('user.login'))


# ==================================================== #
# CREATING USER LOGIN AND LOGOUT OF PROFILE            #
# ==================================================== #
@user_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    role = ''
    if request.method == 'POST':
        if form.validate_on_submit():
            user = User.query.filter_by(email=form.email.data).first()
            if user is not None and user.is_correct_password(form.password.data):
                user.authenticated = True
                user.last_login_date = user.current_login_date
                user.current_login_date = datetime.now()
                db.session.add(user)
                db.session.commit()
                login_user(user)

                flash('Thanks for logging in, {}'.format(current_user.last_name))
                return redirect(url_for('home.index'))
            else:
                flash('ERROR! Incorrect login credentials.', 'error')
    return render_template('login.html', form=form, role=role)


@user_blueprint.route('/logout')
@login_required
def logout():
    user = current_user
    user.authenticated = False
    db.session.add(user)
    db.session.commit()
    logout_user()
    flash('Goodbye!', 'info')
    return redirect(url_for('user.login'))


@user_blueprint.route('/user_profile')
@login_required
def user_profile():
    return render_template('user_profile.html')


# ==================================================== #
# CREATING USER PASSWORD RESET VIA EMAIL               #
# ==================================================== #
def send_password_reset_email(user_email):
    password_reset_serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])

    password_reset_url = url_for(
        'user.password_reset',
        token=password_reset_serializer.dumps(user_email, salt='password-reset-salt'),
        _external=True)

    html = render_template(
        'email_password_reset.html',
        password_reset_url=password_reset_url)

    send_email('Password Reset Requested', [user_email], html)


@user_blueprint.route('/reset/', methods=["GET", "POST"])
def password_reset():
    form = EmailForm(request.form)
    if form.validate_on_submit():
        try:
            user = User.query.filter_by(email=form.email.data).first_or_404()
        except:
            flash('Invalid email address!', 'error')
            return render_template('password_reset.html', form=form)

        if user.email_confirmed:
            send_password_reset_email(user.email)
            flash('Please check your email for a password reset link.', 'success')
        else:
            flash('Your email address must be confirmed before attempting a password reset.', 'error')
        return redirect(url_for('user.login'))

    return render_template('password_reset.html', form=form)


@user_blueprint.route('/reset/<token>', methods=["GET", "POST"])
def reset_with_token(token):
    try:
        password_reset_serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])
        email = password_reset_serializer.loads(token, salt='password-reset-salt', max_age=3600)
    except:
        flash('The password reset link is invalid or has expired.', 'error')
        return redirect(url_for('user.login'))

    form = PasswordForm()

    if form.validate_on_submit():
        try:
            user = User.query.filter_by(email=email).first_or_404()
        except:
            flash('Invalid email address!', 'error')
            return redirect(url_for('user.login'))

        user.password = form.password.data
        db.session.add(user)
        db.session.commit()
        flash('Your password has been updated!', 'success')
        return redirect(url_for('user.login'))

    return render_template('reset_password_with_token.html', form=form, token=token)


@user_blueprint.route('/profile/', methods=['GET', 'POST'])
@login_required
def edit_profile():
    user = current_user
    form = UserProfileForm(request.form)
    if form.validate_on_submit():
        try:
            user.authenticated = True
            user.first_name = form.first_name.data
            user.last_name = form.last_name.data
            user.nick_name = form.nick_name.data
            db.session.add(user)
            db.session.commit()
            flash("Your changes have been saved", 'success')
            return redirect(url_for('user_profile'))
        except:
            flash('your changes were not saved', 'error')
    return render_template('edit_user_profile.html', form=form)
