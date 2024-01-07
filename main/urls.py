from django.urls import path
from . import views
from django.contrib.auth.views import *
import django


urlpatterns = [
    path('', views.homeView),
    path('home', views.homeView, name="home"),
    path('leaderboard', views.showRanking),
    path('sign-up', views.sign_up),
    path('logout', views.logout_view),
    path('games', views.allGames),
    path('games/<slug:slug>', views.loadGame, name="game"),
    path('games/categories/<slug:slug>', views.showByCat),
]
