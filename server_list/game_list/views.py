from django.shortcuts import render


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
    context = {
        'project': 'Ludum Dare Team Bonanza',
    }

    return render(request, 'download.html', context)
