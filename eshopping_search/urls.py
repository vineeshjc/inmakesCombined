from django.urls import path

from . import views

app_name = 'e-search'

urlpatterns = [
    path('eshop_search', views.eshop_search, name='eshop_search'),
]
