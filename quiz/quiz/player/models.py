from django.db import models


class Player(models.Model):
    email = models.EmailField(unique=True, blank=False)

    def __unicode__(self):
        return self.email


class Rank(models.Model):
    player = models.ForeignKey(Player)
    points = models.IntegerField()

    def __unicode__(self):
        return '{0} - {1} points'.format(self.player, self.points)
