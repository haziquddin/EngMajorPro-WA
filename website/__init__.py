from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os
import numpy as np
from os import path
import tensorflow as tf
from tensorflow import keras
from keras.models import load_model
from keras_preprocessing.image import load_img

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = '9OLWxND4o83j4K4iuopO'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from .models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    from .views import view as view_blueprint
    app.register_blueprint(view_blueprint)

    from .predict import predict as predict_blueprint
    app.register_blueprint(predict_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    return app


def create_database(app):
    if not path.exists("website/instance/db.sqlite"):
        db.create_all(app=app)
        print("Created database!")
