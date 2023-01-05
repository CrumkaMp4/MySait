from django.shortcuts import render
from .models import Webdev, Person


def index(request):
    return render(request, 'websait/index.html', {'title': 'Игровой сервер'})


def rules(request):
    tasks = Webdev.objects.order_by('id')
    return render(request, 'websait/rules.html', {'title': 'Правила', 'tasks': tasks})


def moder(request):
    tasks = Person.objects.order_by('id')
    return render(request, 'websait/moder.html', {'title': 'Модерация', 'tasks': tasks})
