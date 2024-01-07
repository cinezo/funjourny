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

def showByCat(request, slug):
    cat = Category.objects.get(slug=slug)
    return render(request, 'main/game_category.html', {
        'category': cat
    })

def allGames(request):
    game = Game.objects.all()
    game_cat = Category.objects.all()
    return render(request, 'main/all-games.html', {
        'game_detail': game,
        'game_category': game_cat,
    })



def loadGame(request, slug):
    game = Game.objects.get(slug=slug)
    try:
        user_score = Ranking.objects.get(player=request.user).game_overall_score
    except:
        user_score = 0
    if request.method == 'POST':
        score = request.POST['newscore']
        new_post_submit = Ranking(player=request.user, game_overall_score=score)
        if int(score) > user_score:
            try:
                new_post_submit.save()
            except:
                new_post_submit.save(update_fields=['game_overall_score'])
    
    return render(request, 'main/game-detail.html', {
        'game': game,
        'user_score': user_score
    })