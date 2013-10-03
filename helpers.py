# -*- coding: utf-8 -*-

from flask import request
from flask import redirect, url_for, make_response


def current_user():
    return request.cookies.get('user')


def set_current_user(user):
    resp = make_response(redirect(url_for('index')))
    expires = None

    if not user:
        expires = 0

    resp.set_cookie('user', user, expires=expires)
    return resp
