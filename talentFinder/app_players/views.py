from datetime import datetime

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse

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


def ajax_edit_player(request, pk):
    data = {}
    data['form_is_valid'] = False
    player = get_object_or_404(Player, pk=pk)
    form = PlayerForm(instance=player)
    data_url = reverse('ajax_edit_player', kwargs={'pk': player.pk})
    if request.method == 'POST':
        form = PlayerForm(request.POST)
        player.name = form.data['name']
        player.last_name = form.data['last_name']
        player.club = form.data['club']
        player.position = form.data['position']
        player.birth_date = datetime.strptime(form.data['birth_date'], '%d-%m-%Y').strftime("%Y-%m-%d")
        player.save()

        data['form_is_valid'] = True

        return JsonResponse(data)


    data['html_form'] = render_to_string(
        'forms/edit_player_form.html',
        {'form': form,
         'data_url': data_url},
        request=request
    )

    return JsonResponse(data)