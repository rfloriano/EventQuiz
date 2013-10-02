#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template
from flask.ext.assets import Environment

app = Flask(__name__)
assets = Environment(app)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.debug = True
    assets.debug = app.debug
    app.run()
