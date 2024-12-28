from django.shortcuts import redirect, render
from django.http import Http404

from movie.models.moviesModels import MoviesModels

from .forms import SearchMovieForms

def Home(request):
    movies = MoviesModels.objects.all()
    context = {
        "movies":movies
    }

    return render(request,'home/index.html',context)

def Details(request,movies_id):
    try:
        movies = MoviesModels.objects.get(pk=movies_id)
        context = {
            "movies":movies
        }
    except MoviesModels.DoesNotExist:
        raise Http404("Movies Not Found")
    
    return render(request,'home/details.html',context)

def Search(request):
    if request.method == 'POST':
        form = SearchMovieForms(request.POST)
        if form.is_valid():
            movies_name = form.cleaned_data['movie_name']
            results = MoviesModels.objects.filter(moviesName__icontains='{s}'.format(s=movies_name))
            context = {
                "results":results,
                "form":form
            }
            return render(request,'home/results.html',context)
    else:
        form = SearchMovieForms()
        results = MoviesModels.objects.all()
        context = {
            "results":results,
            "form":form
        }
        return render(request,'home/results.html', context)