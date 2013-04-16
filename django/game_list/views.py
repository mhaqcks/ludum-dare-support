from django.shortcuts import render
from django.http import HttpResponse
import os
import random
import json
import bios

FILE_ROOT = os.path.normpath(os.path.dirname(os.path.realpath(__file__)))


def chunks(l, n):
    """ Yield successive n-sized chunks from l.
    """
    print(l)
    for i in range(0, len(l), n):
        yield l[i:i+n]


def home(request):

    context = {
        'project': 'Ludum Dare Team Bonanza',
    }

    return render(request, 'index.html', context)


def about(request):

    random.shuffle(bios.BIOS)
    context = {
        'project': 'Ludum Dare Team Bonanza',
        'bios': chunks(bios.BIOS, 3),
    }
    print(context['bios'])

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
    {"game_number": 10, "game_name": "Max max max max max max", "players": "5/5", "status": "S'all good", "locked": True},
]


def games(request):

    content = JSON
    print(request.POST)
    print(request.GET)
    print(request.method)
    print(request.body)
    game_number = request.POST['game_number']
    game_name = request.POST['game_name'].lower()
    players = request.POST['players'].lower()
    locked = request.POST['locked'].lower()
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


def retrieve_game(request):
    print(request.POST)
    error = None
    if int(request.POST['game_number']) == -1:
        error = 'That is an invalid password!'
    content = json.dumps({
        'error': error,
        'connect_info': 'jacobvgardner.com/server/yep',
        })
    return HttpResponse(content, content_type='application/json')


def gadget(request):
    return render(request, 'gadget.xml')
