# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url
from views import SessionView

urlpatterns = patterns(
    '',
    url(r'^session/', SessionView.as_view(), name='session'),
)
