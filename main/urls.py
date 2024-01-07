from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomeView.as_view()),
    path('home', views.HomeView.as_view(), name="home"),
    path('sign-up', views.sign_up),
    path('logout', views.logout_view),
    path('games', views.allGames),
    path('games/<slug:slug>', views.loadGame),
    path('<slug:slug>', views.showByCat),
]
