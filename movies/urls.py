from django.urls import path
from . import views


app_name = 'movies'


urlpatterns = [
    path('', views.index, name='index'),  # 영화목록
    path('<int:movie_id>/', views.detail, name='detail'),
    path('create/', views.create, name='create'),  # 2개 method 로 분기
    path('<int:movie_id>/update/', views.update, name='update'),  # 2개 method 로 분기
    path('<int:movie_id>/delete/', views.delete, name='delete'),  # POST 로 들어왔을 때만 삭제
]

