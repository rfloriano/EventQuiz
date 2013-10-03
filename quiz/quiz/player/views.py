#!/usr/bin/env python

from django.views.generic import TemplateView
# from models import Player


class SessionView(TemplateView):
    template_name = 'player/session.html'
