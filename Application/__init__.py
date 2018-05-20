from flask import Flask

app = Flask(__name__)

# Registering Application

from .home.views import home_blueprint
from .admin.views import admin_blueprint
from .lexicon.views import lexicon_blueprint

app.register_blueprint(home_blueprint)
app.register_blueprint(admin_blueprint)
app.register_blueprint(lexicon_blueprint)