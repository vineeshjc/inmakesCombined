from django import forms

from todo_app.models import todo_db


class todo_form(forms.ModelForm):
    class Meta:
        model = todo_db
        fields = ['name', 'level', 'created']

