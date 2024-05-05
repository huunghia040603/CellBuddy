import math
from flask import render_template, request, redirect, session, jsonify
import dao
import utils
from CellPhone import app, login
from flask_login import login_user, logout_user, login_required


@app.route('/')
def index():
    return render_template('index.html')


@login.user_loader
def get_user(user_id):
    return dao.get_user_by_id(user_id)


if __name__ == '__main__':
    from CellPhone import admin
    app.run(debug=True)
