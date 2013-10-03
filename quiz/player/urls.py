# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url
from views import SessionView

urlpatterns = patterns(
    '',
    url(r'', SessionView.as_view(), name='session'),
)
