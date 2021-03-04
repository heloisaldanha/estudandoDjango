from django.shortcuts import render
from django.http import HttpResponse
# HttpResponse é só pra dar uma resposta na tela
# views é onde cria o método que acontece na página


# sempre vem essas requests por convenção
def index(request):
    return HttpResponse('Olá mundo!')
