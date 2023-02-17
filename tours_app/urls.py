from django.urls import path

from tours_app import views

app_name = 'traveller'

urlpatterns = [
    path('index', views.travel_index, name='travel_index'),
    path('destinations', views.travel_destinations, name='destinations'),
    path('elements', views.travel_elements, name='elements'),
    path('news', views.travel_news, name='news'),
    path('contact', views.travel_contact, name='contact'),
    path('header_update/<int:id>/', views.header_update, name='header_update'),
    path('banner_update/<int:id>/', views.banner_update, name='banner_update'),
    path('footer_update/<int:id>/', views.footer_update, name='footer_update'),
    path('our_team_update/<int:id>/', views.our_team_update, name='our_team_update'),
]
