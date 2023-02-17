from django.urls import path

from register_app import views

app_name = 'registry'

urlpatterns = [
    path('register', views.add_user, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout')
]
