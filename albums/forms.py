from dataclasses import fields
from django import forms
from django.forms import ModelForm
from .models import Album

class CreateAlbumForm(ModelForm):
    class Meta:
        model = Album
        fields = [
            'name',
            'artist',
            'release_datetime',
            'cost',
            'is_approved'
        ]
        widgets = {
            'release_datetime': forms.DateInput(format=('%m/%d/%Y'), attrs={'type':'date'}),
        }