from django.shortcuts import render, redirect
from .models import Movies
from .forms import MoiveForm

# Create your views here.


def index(request):
    movies = Movies.objects.order_by("-pk")
    context = {
        "movies": movies,
    }
    return render(request, "movie/index.html", context)


def create(request):
    if request.method == "POST":
        movie_form = MoiveForm(request.POST)
        if movie_form.is_valid():
            movie_form.save()
            return redirect("movie:index")
    else:
        movie_form = MoiveForm()
    context = {
        "movie_form": movie_form,
    }
    return render(request, "movie/create.html", context=context)


def detail(request, pk):
    movie = Movies.objects.get(pk=pk)
    context = {
        "movie": movie,
    }
    return render(request, "movie/detail.html", context)


def update(request, pk):
    movie = Movies.objects.get(pk=pk)
    if request.method == "POST":
        movie_form = MoiveForm(request.POST, instance=movie)
        if movie_form.is_valid():
            movie_form.save()
            return redirect("movie:detail", movie.pk)
    else:
        movie_form = MoiveForm(instance=movie)
    context = {
        "movie_form": movie_form,
        "movie": movie,
    }
    return render(request, "movie/create.html", context)


def delete(request, pk):
    movie = Movies.objects.get(pk=pk)
    movie.delete()
    return redirect("movie:index")
