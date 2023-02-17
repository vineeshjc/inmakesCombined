from django import forms

from movies_app.models import movies_mod


class movie_form(forms.ModelForm):
    class Meta:
        model = movies_mod
        fields = ['name', 'story', 'released', 'image']
