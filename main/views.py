from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import login

from tictactoe.models import Game

@login_required
def home(request):
    my_games = Game.objects.games_for_user(request.user)
    active_games = my_games.filter(status="A")
    finished_games = my_games.exclude(status="A")
    waiting_games = active_games.filter(next_to_move = request.user)
    other_games = active_games.exclude(next_to_move = request.user)
    context = {'other_games' : other_games,
               'waiting_games' : waiting_games,
               'finished_games' : finished_games}
    return render(request, "main/home.html",context)

@login_required
def newGame(request):
    return render(request, 'tictactoe/newGame.html')
