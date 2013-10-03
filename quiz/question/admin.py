from django.contrib import admin
from quiz.question.models import Question, Answer


class AnswerInline(admin.TabularInline):
    model = Answer
    max_num = 3


class QuestionAdmin(admin.ModelAdmin):
    model = Question
    inlines = [AnswerInline]


admin.site.register(Question, QuestionAdmin)
