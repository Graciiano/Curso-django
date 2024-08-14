from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'recipes/home.html', context={
        'name': 'Diogo Graciano'
    })

def contact(request):
    return HttpResponse('CONTATO')

def sobre(request):
    return HttpResponse('SOBRE')
