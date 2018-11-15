from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

from shop.models import Game

# Create your views here.
def index(request):
    if request.method == 'GET':
        
        
        return HttpResponse('Hello my name is saidjillo')



