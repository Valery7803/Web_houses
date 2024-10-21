from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'houses/index.html')


def about(request):
    return render(request, 'houses/about.html')


def contacts(request):
    return render(request, 'houses/contacts.html')


def show_house(request, show_id):
    return HttpResponse(f'Обзор дома с {show_id}')


def login(request):
    return HttpResponse('Авторизация')
