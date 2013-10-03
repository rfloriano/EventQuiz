from django.db import models


class Question(models.Model):
    question = models.CharField(max_length=255)


class Answer(models.Model):
    anwaer = models.CharField(max_length=255)
    is_right = models.BooleanField(default=False)
    question = models.ForeignKey(Question)
