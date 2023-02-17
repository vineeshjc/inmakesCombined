from django import forms

from tours_app.models import header_back, banner_back, footer_back, our_team


class header_form(forms.ModelForm):
    class Meta:
        model = header_back
        fields = ['name', 'image']


class banner_form(forms.ModelForm):
    class Meta:
        model = banner_back
        fields = ['name', 'image']


class footer_form(forms.ModelForm):
    class Meta:
        model = footer_back
        fields = ['name', 'image']


class team_form(forms.ModelForm):
    class Meta:
        model = our_team
        fields = ['name', 'image', 'detail']
