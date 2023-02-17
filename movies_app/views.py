from django.shortcuts import render, redirect

from movies_app.forms import movie_form
from movies_app.models import movies_mod


def list_movies(request):
    movies = movies_mod.objects.all()
    return render(request, 'movies.html', {'movies': movies})


def add_movie(request):
    if request.method == 'POST':
        name = request.POST.get('name', )
        story = request.POST.get('story', )
        released = request.POST.get('released', )
        image = request.FILES['image']
        film = movies_mod(name=name, story=story, released=released, image=image)
        film.save()
    return render(request, 'add_movie.html')


def movie_details(request, id):
    movie = movies_mod.objects.get(id=id)
    return render(request, 'movie_details.html', dict(movie=movie))


def movie_delete(request, id):
    movie = movies_mod.objects.get(id=id)
    if request.method == 'POST':
        movie.delete()
        return redirect('movie:list_movies')
    return render(request, 'delete_movie.html', dict(movie=movie))


def movie_update(request, id):
    movie = movies_mod.objects.get(id=id)
    form = movie_form(request.POST or None, request.FILES, instance=movie)
    if form.is_valid():
        form.save()
        return redirect('movie:list_movies')
    return render(request, 'movie_update.html', dict(movie=movie, form=form))
