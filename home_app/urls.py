from django.urls import path

from home_app import views

urlpatterns = [
    path('', views.main, name='main'),
]
