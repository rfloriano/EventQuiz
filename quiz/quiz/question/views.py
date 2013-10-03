#!/usr/bin/env python

from django.views.generic import ListView
#from django.views.generic import TemplateView
from models import Question


class GameView(ListView):
    model = Question

