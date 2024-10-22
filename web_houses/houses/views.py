from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

menu = [
    'Главная страница', 'Страница про нас', 'Наши контакты', 'Авторизация'
]

# Представление 'главной страницы'
def index(request):
    return render(request, 'houses/index.html')

# Представление 'страницы про нас'
def about(request):
    return render(request, 'houses/about.html')

# Представление страницы 'наши контакты'
def contacts(request):
    return render(request, 'houses/contacts.html')

# Представление страницы 'обзора дома'
def show_house(request, show_id):
    return HttpResponse(f'Обзор дома с {show_id}')

def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

# Страница 'авторизации'
def login(request):
    return HttpResponse('Авторизация')
