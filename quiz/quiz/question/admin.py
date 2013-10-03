from django.contrib import admin
from quiz.question.models import Question, Answer


class AnswerInline(admin.StackedInline):
    model = Answer


class QuestionAdmin(admin.ModelAdmin):
    model = Question
    inlines = [AnswerInline]


admin.site.register(Question, QuestionAdmin)
