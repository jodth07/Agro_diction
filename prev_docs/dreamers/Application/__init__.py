from flask import Flask, render_template
from flask_mail import Mail
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


# app = Flask(__name__)

app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('flask.cfg')
app.secret_key = 'djal;sjf;sljf;lsjflsjflaj'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
mail = Mail(app)
migrate = Migrate(app, db)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "user.login"

############################
# custom error pages       #
############################


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(403)
def page_not_found(e):
    return render_template('403.html'), 403


@app.errorhandler(410)
def page_not_found(e):
    return render_template('410.html'), 410


# Local Blueprint Imports #
from .user.models import User
from .home.views import home_blueprint
from .article.views import article_blueprint
from .blog.views import blog_blueprint
from .dictionary.views import dict_blueprint
from .user.views import user_blueprint
from .contact.views import contact_blueprint
from .admin.views import admin_blueprint


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter(User.id == int(user_id)).first()


# register the blueprints
app.register_blueprint(home_blueprint)
app.register_blueprint(article_blueprint)
app.register_blueprint(blog_blueprint)
app.register_blueprint(dict_blueprint)
app.register_blueprint(user_blueprint)
app.register_blueprint(contact_blueprint)
app.register_blueprint(admin_blueprint)


if __name__=="__main__":
    app.run(debug=True)
