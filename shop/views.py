from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

from shop.models import Game

# Create your views here.
def index(request):
    if request.method == 'GET':
        print(request.body)
        
        return HttpResponse('Hello my name is saidjillo')

def get_games(request):
    if request.method == 'GET':
        games  = Game.objects.all()[0]

        return HttpResponse(f'All games from the database are here {games} --> {games.id} {games.title} {games.price}')

def get_html(request):
    
    if request.method == 'GET':
        return render(request, 'shop/index.html')


