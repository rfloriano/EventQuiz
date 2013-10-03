#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, redirect, url_for, make_response
from flask.ext.assets import Environment

from event_model import auth_user
from helpers import current_user, set_current_user

app = Flask(__name__)
assets = Environment(app)


@app.route('/')
def index():
    if not current_user():
        return redirect(url_for('login'))

    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST' and auth_user(request.form.get('login')):
        return set_current_user(request.form.get('login'))

    return render_template('login.html')


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    return set_current_user('')
    #return render_template('logout.html')


@app.context_processor
def utility_processor():
    return dict(current_user=current_user)


if __name__ == '__main__':
    app.debug = True
    assets.debug = app.debug
    app.run()
