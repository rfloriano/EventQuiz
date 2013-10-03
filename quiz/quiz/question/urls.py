# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url
from views import GameView

urlpatterns = patterns(
    '',
    url(r'^game/', GameView.as_view()),
)

