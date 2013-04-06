from django.shortcuts import render
from django.http import HttpResponse
import os
import random
import json

FILE_ROOT = os.path.normpath(os.path.dirname(os.path.realpath(__file__)))


def home(request):

    context = {
        'project': 'Ludum Dare Team Bonanza',
    }

    return render(request, 'index.html', context)


def about(request):
    context = {
        'project': 'Ludum Dare Team Bonanza',
    }

    return render(request, 'about.html', context)


def status(request):
    context = {
        'project': 'Ludum Dare Team Bonanza',
    }

    return render(request, 'status.html', context)


def download(request):

    icons = random.sample(
        os.listdir(os.path.join(FILE_ROOT, 'static', 'img', 'os_icons')), 3)

    context = {
        'project': 'Ludum Dare Team Bonanza',
        'icon': icons
    }

    return render(request, 'download.html', context)

JSON = [
    {"game_number": -1, "game_name": "This is a game name!!", "players": "2/5", "status": "Particularly Slutty", "locked": True},
    {"game_number": -2, "game_name": "This is not a game name!!", "players": "5/5", "status": "Ummm... Good, I guess.", "locked": False},
    {"game_number": 53, "game_name": "Emily", "players": "1/3", "status": "Yeap", "locked": False},
    {"game_number": 54, "game_name": "Misty", "players": "2/3", "status": "Status Here", "locked": False},
    {"game_number": 55, "game_name": "Keelie", "players": "3/3", "status": "LKFJLDKF LKFJLkdflkdajfk", "locked": False},
    {"game_number": 57, "game_name": "Misty <3 Keelie 4 Evar", "players": "99/100", "status": "Hmmmmmmm", "locked": False},
    {"game_number": 59, "game_name": "Jacob <3 Emily", "players": "5/100", "status": "S'all good", "locked": True},
]


def games(request):

    content = JSON
    game_number = request.GET['game_number']
    game_name = request.GET['game_name'].lower()
    players = request.GET['players'].lower()
    locked = request.GET['locked'].lower()
    print(game_number, game_name, players, locked)
    if game_number:
        game_number = int(game_number)
        for row in content:
            if int(row['game_number']) == game_number:
                content = [row]
                break

    rows = []
    if game_name:
        for row in content:
            if game_name in row['game_name'].lower():
                rows += [row]

        content = rows

    rows = []
    if players == 'hide full games':
        for row in content:
            n, m = row['players'].split('/')
            if n != m:
                rows += [row]

        content = rows

    rows = []
    if locked != 'all':
        for row in content:
            if locked == 'public' and not row['locked']:
                rows += [row]
            elif locked == 'private' and row['locked']:
                rows += [row]

        content = rows

    content = json.dumps({'gamedata': content})
    return HttpResponse(content, content_type='application/json')
    #return render(request, 'gamelist.json', content_type='application/json')
