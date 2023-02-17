from django.urls import path

from movies_app import views

app_name = 'movie'

urlpatterns = [
    path('list_movies', views.list_movies, name='list_movies'),
    path('add_movie', views.add_movie, name='add_movie'),
    path('movie_details/<int:id>/', views.movie_details, name='movie_details'),
    path('delete_movie/<int:id>/', views.movie_delete, name='delete_movie'),
    path('update_movie/<int:id>/', views.movie_update, name='update_movie'),
]
