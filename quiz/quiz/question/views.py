#!/usr/bin/env python

from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from models import Question, Answer


class GameView(TemplateView):
    model = Question
    template_name = 'question/game.html'
    seen_questions = {}

    def get_context_data(self, **kwargs):
        context = super(GameView, self).get_context_data(**kwargs)
        context['current_question'] = None

        seen_questions = GameView.seen_questions.keys()
        in_game = self.request.session.get('in_game', True)

        qs = Question.objects.exclude(pk__in=seen_questions)

        if qs.exists() and in_game:
            context['current_question'] = qs.order_by('?')[0]

        return context

    def post(self, request, *args, **kwargs):
        answer = Answer.objects.get(pk=request.POST['answer_id'])
        request.session['in_game'] = answer.is_right

        GameView.seen_questions[answer.question_id] = True

        return HttpResponseRedirect(reverse('game_index'))

