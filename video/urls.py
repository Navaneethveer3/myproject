# video/urls.py

from django.urls import path
from . import views

app_name = 'video'

urlpatterns = [
    path('', views.myproject, name='myproject'),
    path('get_video_qualities/', views.get_video_qualities, name='get_video_qualities'),
    path('download_video/', views.download_video, name='download_video'),
    path('media/<str:filename>/', views.serve_file, name='serve_file'),
]
