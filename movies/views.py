from django.http import HttpResponse, Http404
from django.shortcuts import render, get_list_or_404
from .models import Movie

# Create your views here.


def index(request):
    movies = Movie.objects.all()
    # output = ', '.join([m.title for m in movies])
    return render(request, 'movies/index.html', {'movies': movies})

    # SELECT * FROM movies_movie
    # Movie.objects.filter(release_year=1984)
    # # SELECT * FROM movies_movie WHERE
    # Movie.objects.get(id=1)

    # return HttpResponse(output)


def detail(request, movie_id):
    # try:
    movie = get_list_or_404(Movie, pk=movie_id)
    # movie = Movie.objects.get(pk=movie_id)  # id = pk [primary key]
    # return HttpResponse(movie_id)
    return render(request, 'movies/detail.html', {'movie': movie})
    # except Movie.DoesNotExist:
    #     raise Http404()
