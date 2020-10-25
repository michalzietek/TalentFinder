from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from app_players.forms import PlayerForm
from app_players.models import Player


def players_list(request):
    players = Player.objects.all()
    return render(request, 'players_list.html', {
        'players': players
    })


def add_player(request):
    if request.method == 'POST':
        form = PlayerForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            players = Player.objects.all()
            return render(request, 'players_list.html', {
                'players': players
            })
    else:
        form = PlayerForm()
    return render(request, 'add_player.html', {'player': form})


def ajax_delete_player(request):
    player_id = request.GET.get('player') or None
    player = get_object_or_404(Player, pk=player_id)
    player.delete()

    return HttpResponse('')
