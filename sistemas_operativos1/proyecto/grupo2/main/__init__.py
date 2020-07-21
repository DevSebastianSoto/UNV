import os

import jinja2
from flask import Flask

from main.routes import r_base


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile(os.path.join('..', 'config.cfg'))
    template_dir = os.path.join('.', 'templates')
    app.register_blueprint(r_base)
    loader = jinja2.FileSystemLoader(os.path.join('.', template_dir))
    environment = jinja2.Environment(loader=loader)
    if app.app_context():
        return app
