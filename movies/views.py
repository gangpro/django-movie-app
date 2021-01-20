from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods, require_GET, require_POST
from .models import Movie


# 영화 리스트를 index.html 로 넘겨줘야 함.
def index(request):
    movies = Movie.objects.all()
    context = {'movies': movies}
    return render(request, 'movies/index.html', context)


# movie_id 에 맞는 movie 데이터를 넘겨줘야 함.
def detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    context = {'movie': movie}
    return render(request, 'movies/detail.html', context)


def create(request):
    # GET /movies/create/
    if request.method == 'GET':
        # html 렌더링
        return render(request, 'movies/create.html')
    # POST /movies/create/
    else:
        title = request.POST.get('title')
        title_origin = request.POST.get('title_origin')
        vote_count = request.POST.get('vote_count')
        open_date = request.POST.get('open_date')
        genre = request.POST.get('genre')
        score = request.POST.get('score')
        poster_url = request.POST.get('poster_url')
        description = request.POST.get('description')

        movie = Movie()
        movie.title = title
        movie.title_origin = title_origin
        movie.vote_count = vote_count
        movie.open_date = open_date
        movie.genre = genre
        movie.score = score
        movie.poster_url = poster_url
        movie.description = description
        movie.save()

        return redirect('movies:detail', movie.pk)


def update(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    if request.method == 'GET':
        context = {'movie': movie}
        return render(request, 'movies/update.html', context)
    else:
        title = request.POST.get('title')
        title_origin = request.POST.get('title_origin')
        vote_count = request.POST.get('vote_count')
        open_date = request.POST.get('open_date')
        genre = request.POST.get('genre')
        score = request.POST.get('score')
        poster_url = request.POST.get('poster_url')
        description = request.POST.get('description')

        movie.title = title
        movie.title_origin = title_origin
        movie.vote_count = vote_count
        movie.open_date = open_date
        movie.genre = genre
        movie.score = score
        movie.poster_url = poster_url
        movie.description = description
        movie.save()
        return redirect('movies:detail', movie.id)


def delete(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    movie.delete()
    return redirect(request, 'movies:index')

