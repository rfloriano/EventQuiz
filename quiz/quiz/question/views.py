#!/usr/bin/env python

from django.views.generic import ListView
#from django.views.generic import TemplateView
from django.shortcuts import redirect
from models import Question


class GameView(ListView):
    model = Question

    def get(self, request, *args, **kwargs):
        if not request.session.get('player', False):
            return redirect('session')
        return super(GameView, self).get(request, *args, **kwargs)
