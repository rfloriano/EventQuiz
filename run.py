#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, redirect, url_for, make_response
from flask.ext.assets import Environment

from event_model import auth_user

app = Flask(__name__)
assets = Environment(app)


@app.route('/')
def index():
    user = request.cookies.get('user')

    if not user:
        return redirect(url_for('login'))

    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST' and auth_user(request.form.get('login')):
        resp = make_response(redirect(url_for('index')))
        resp.set_cookie('user', request.form.get('login'))
        return resp

    return render_template('login.html')


if __name__ == '__main__':
    app.debug = True
    assets.debug = app.debug
    app.run()
