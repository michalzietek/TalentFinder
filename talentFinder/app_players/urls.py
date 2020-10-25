from django.urls import re_path
from .views import players_list, add_player, ajax_delete_player

urlpatterns = [
    re_path('^list/$', players_list, name='players_list'),
    re_path('^add/$', add_player, name='add_player'),
    re_path('^delete/$', ajax_delete_player, name='delete_player'),
    ]