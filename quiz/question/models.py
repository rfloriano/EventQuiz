from django.db import models


class Question(models.Model):
    question = models.CharField(max_length=255)

    def __unicode__(self):
        return self.question


class Answer(models.Model):
    answer = models.CharField(max_length=255)
    is_right = models.BooleanField(default=False)
    question = models.ForeignKey(Question)

    def __unicode__(self):
        return self.answer
