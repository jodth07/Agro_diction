from flask import Flask

app = Flask(__name__)

# Registering Application

from .home.views import home_blueprint

app.register_blueprint(home_blueprint)