from django.db import models


class Player(models.Model):
    email = models.EmailField()

    def __unicode__(self):
        return self.email


class Rank(models.Model):
    player = models.ForeignKey(Player)
    points = models.IntegerField()

    def __unicode__(self):
        return '%s - %d points'.format(self.player, self.points)
