from django.forms import forms,ModelForm
from .models import Room


class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = "__all__"
        exclude = ['host','participants']