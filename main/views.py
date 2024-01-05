from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .forms import RegisterForm
from .models import *
from django.contrib.auth import login, logout, authenticate
# Create your views here.


class HomeView(TemplateView):
    template_name = 'main/home.html'



def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('/home')
    else:
        form = RegisterForm()
    
    return render(request, 'registration/sign_up.html', {
        'form': form
    })
def logout_view(request):
    logout(request)

def allGames(request):
    game = Game.objects.all()
    return render(request, 'main/all-games.html', {
        'game_detail': game
    })

def loadGame(request, slug):
    game = Game.objects.get(slug=slug)
    return render(request, 'main/game-detail.html', {
        'game': game
    })