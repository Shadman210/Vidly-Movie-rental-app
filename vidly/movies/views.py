from django.shortcuts import render, HttpResponse
from django.http import Http404
from .models import Movie

def index(request):
	movies = Movie.objects.all()
	return render(request, "movies/index.html", {'movies': movies})

def details(request, movie_Id):
	try:
		movie = Movie.objects.get(id=movie_Id)
		return render(request, 'movies/details.html', {'movie': movie})
	except Movie.DoesNotExist:
		raise Http404

