from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_mail import Message
from sqlalchemy.exc import IntegrityError

# Local Imports
from Application import mail
from .forms import MailForm


contact_blueprint = Blueprint('contact', __name__, template_folder='templates')


@contact_blueprint.route('/contact/', methods=['GET', 'POST'])
def contact_us():
    form = MailForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            try:
                name = form.first_name.data + " " + form.last_name.data
                email = form.email.data
                message_content = name + " \n" + email + " \n" + form.message.data
                msg = Message(
                        form.title.data,
                        body=message_content,
                        recipients=["olsonpho@gmail.com"]
                    )
                msg.add_recipient = [form.email.data]
                mail.send(msg)
                flash('Thank you for contacting us. You should hear back shortly', 'success')
                return redirect(url_for("contact.contact_us"))
            except IntegrityError:
                flash('ERROR! Email not sent. please completely fill this out.')
    return render_template("contact_us.html", form=form)
