from django.urls import re_path
from .views import players_list

urlpatterns = [
    re_path('list/', players_list, name='players_list')
    ]