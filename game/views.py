from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from django.urls import reverse
from .models import Game

# declared two global variables for current player
global_name = ""
global_id = 35

def home(request):
    context={}
    return render(request,"start.html",context) 

def newgame(request):
    return render(request,"newgame.html")

def menupage(request):
    player= Game.objects.all().values()
    context={
        'player':player,
    }
    return render(request,"menu-page.html",context)
    # return render(request,"menu-page.html")

# def loadgame(request):
#     player= Game.objects.all().values()
#     context={
#         'player':player,
#     }
#     return render(request,"menu-page.html",context)

# def scoreboard(request):
#     player= Game.objects.all().values()
#     context={
#         'player':player,
#     }
#     return render(request,"menu-page.html",context)

# adding a fucntion to save the score of a player.
def backtomenu(request):
    s = request.POST['score']
    player = Game.objects.get(id = global_id) 
    player.score = s
    player.save()
    return HttpResponseRedirect(reverse('menupage'))

#changes to addplayer function
def addplayer(request):
    global global_name
    global_name = request.POST['name']
    player = Game(name=global_name,score=0)
    player.save()
    global global_id 
    global_id = player.id
    return HttpResponseRedirect(reverse('index'))

def index(request):
    player = Game.objects.get(id=global_id) 
    context = {
        'player' : player
    }
    return render(request,"index.html",context)

def delete(request,id):
    player = Game.objects.get(id=id) 
    player.delete()
    return HttpResponseRedirect(reverse('menupage'))

def continuegame(request,id):
    global global_id 
    global_id = id
    return HttpResponseRedirect(reverse('index'))

def quit(request):
    return render(request,"/")

