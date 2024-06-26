# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from logging import root
from flask import Flask
from flask_login import LoginManager
import pymysql
from importlib import import_module
from dotenv import load_dotenv
 # Get the current directory
login_manager = LoginManager()
def register_extensions(app):
    login_manager.init_app(app)
def register_blueprints(app):
    for module_name in ('authentication', 'home'):
        try:
            module = import_module('apps.{}.authentication_blueprint'.format(module_name))
        except:
            module = import_module('apps.{}.routes'.format(module_name))
        finally:
            app.register_blueprint(module.blueprint)
def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    register_extensions(app)
    register_blueprints(app)
    return app
