from socket import SocketIO
import numpy as np
import info
from flask import render_template


def login_start():
        form = info.LoginForm()
        return render_template("./login.html", template_title="login", LForm = form)
    
if __name__ == '__main__': 
    login_start()