from django import forms

from eshopping_app.models import categories_db, products_db


class categories_form(forms.ModelForm):
    model = categories_db
    fields = ['name', 'slug', 'details', 'image']


class products_form(forms.ModelForm):
    model = products_db
    fields = ['name', 'slug', 'details', 'image', 'price', 'stock', 'available']
