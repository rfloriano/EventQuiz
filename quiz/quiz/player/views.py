#!/usr/bin/env python

from django.views.generic import TemplateView
from django.shortcuts import redirect
from models import Player


class SessionView(TemplateView):
    template_name = 'player/session.html'

    def post(self, request):
        email = request.POST.get('email', None)
        if not email:
            raise Exception('An e-mail need to be provided')

        player, _ = Player.objects.get_or_create(email=email)
        request.session['player'] = player.email
        return redirect('game')
