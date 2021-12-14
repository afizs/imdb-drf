from django.http.response import JsonResponse
from django.shortcuts import render
from watchlist_app.models import Movie

# Create your views here.
def movie_list(request):
    movie_list = Movie.objects.all()
    data = {"movies": list(movie_list.values())}
    return JsonResponse(data)

def movie_details(request, pk=None):
    movie = Movie.objects.get(pk=pk)
    data = {"name": movie.name, 'description': movie.description}
    return JsonResponse(data)