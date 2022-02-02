from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Game
from .models import Room
# Create your views here.


L = ["X", "O"]
NL = L.copy()


def prefrences():
    global NL
    if len(NL) == 0:
        NL = L.copy()
    tu = NL.pop(0)
    return tu


def home(request):
    if request.method == "POST":
        username = request.POST.get('username')
        option = request.POST.get('option')
        room_code = request.POST.get('room_code')
        # prefrence = request.POST.get('prefrence')
        prefrence = prefrences()
        if option == '1':
            game = Game.objects.filter(room_code=room_code).first()
            if game is None:
                messages.success(request, "Room code not found")
                return redirect('/')

            if game.is_over:
                messages.success(request, "Game is over")
                return redirect('/')

            game.game_opponent = username
            game.prefrence = prefrence
            game.save()
            print(room_code, username)
            return redirect('/play/' + room_code + '?prefrence='+prefrence)
            # return redirect('/play/' + room_code + '?username='+username)
        else:
            game = Game(game_creator=username, room_code=room_code, prefrence=prefrence)
            game.save()
            room = Room(room=room_code)
            room.save()
            print(room_code, username)
            return redirect('/play/' + room_code + '?prefrence='+prefrence)
    return render(request, "index.html")


def playgame(request, room_code):
    prefrence = request.GET.get('prefrence')
    print(f"username is............{prefrence}")
    context = {
        "room_code": room_code,
        'username': prefrence
        }
    return render(request, "play.html", context)
