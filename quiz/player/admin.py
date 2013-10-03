from django.contrib import admin
from quiz.player.models import Player, Rank


class PlayerAdmin(admin.ModelAdmin):
    model = Player


class RankAdmin(admin.ModelAdmin):
    model = Rank


admin.site.register(Player, PlayerAdmin)
admin.site.register(Rank, RankAdmin)
