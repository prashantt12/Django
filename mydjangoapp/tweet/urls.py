from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.tweetList, name = 'tweetList'),
    path('create/', views.createTweet, name = 'createTweet'),
    path('<int:tweet_id>/delete/', views.delTweet, name = 'delTweet'),
    path('<int:tweet_id>/edit/', views.editTweet, name = 'editTweet'),
    path('register/', views.userRegister, name = 'userRegister'),
]