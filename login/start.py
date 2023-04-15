from socket import SocketIO
import numpy as np
from flask import render_template
from forms import LoginForm
import app


def login_start():
    form = LoginForm()
    print("in start abt to render")
    return render_template("./login.html", template_title="login", Login=form)


if __name__ == '__login__':
    login_start()
