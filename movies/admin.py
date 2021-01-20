from django.contrib import admin
from .models import Movie


# admin 페이지 board 게시판 뷰 설정
class MovieAdmin(admin.ModelAdmin):
    list_display = ['title', 'title_origin', 'vote_count','genre', 'score', 'open_date']


# Register your models here.
admin.site.register(Movie, MovieAdmin)
