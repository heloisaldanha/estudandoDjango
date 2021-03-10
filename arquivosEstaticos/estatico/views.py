from django.shortcuts import render


def index(request):
    return render(request, 'estatico/index.html')


def sobre(request):
    return render(request, 'estatico/sobre.html')

