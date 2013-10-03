# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^question/', include('quiz.question.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include('quiz.player.urls')),
)
