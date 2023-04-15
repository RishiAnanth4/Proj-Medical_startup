from flask import Flask, abort, render_template, url_for, redirect, request
from flask_login import LoginManager
from os import environ
from flask_socketio import SocketIO, emit
from flask_sesion import Session


def create_app():
    app = Flask(__name__)
    Session(app)
    login_manager.init_app(app)
    socketio.init_app(app)
    return app
