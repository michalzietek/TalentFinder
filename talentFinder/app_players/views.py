from django.shortcuts import render

from app_players.models import Player


def players_list(request):
    players = Player.objects.all()
    return render(request, 'players_list.html', {
        'players': players
    })
