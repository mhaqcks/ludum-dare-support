from django.shortcuts import render
import os
import random

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


def games(request):
    return render(request, 'gamelist.json', content_type='application/json')
