from django.contrib import admin
from django.urls import path
from game import views

urlpatterns = [
    path("", views.home, name="start"),
    path("newgame",views.newgame, name="newgame"),
    path("menu-page",views.menupage, name="menupage"),
    path("addplayer",views.addplayer, name="addplayer"),
    # path("loadgame",views.loadgame, name="loadgame"),
    # path("scoreboard",views.scoreboard, name="scoreboard"),
    path("index",views.index, name="index"),
    path("delete/<int:id>",views.delete, name="delete"),
    path("continuegame/<int:id>",views.continuegame, name="continuegame"),
    path("quit",views.home, name="quit"), 
    #adding the save score function
    path("backtomenu",views.backtomenu,name="score"),
]