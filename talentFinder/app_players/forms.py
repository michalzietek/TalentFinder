from django.forms import ModelForm
from django import forms

from app_players.models import Player


class PlayerForm(ModelForm):
    class Meta:
        model = Player
        fields = ['name', 'last_name', 'position', 'club', 'birth_date']

    def __init__(self, *args, **kwargs):

        super(PlayerForm, self).__init__(*args, **kwargs)
        self.fields['birth_date']= forms.DateField()
        self.fields['birth_date'].widget = forms.DateInput(format=('%d-%m-%Y'))
