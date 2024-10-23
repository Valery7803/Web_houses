from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

menu = [
    'Главная страница', 'Страница про нас', 'Наши контакты', 'Авторизация'
]

data_db = [
    {'id': 1, 'title': 'Коттедж «Ривьера 1»', 
     'context':'Премиальные двухэтажные коттеджи «Ривьера»: панорамные окна, просторная терраса и два отдельных входа',
     'prise': '7 474 050₽'},
    {'id': 2, 'title': 'Коттеджи «Император 1»', 
     'context': 'Коттеджи «Император» — строгая геометрия, просторные помещения и никаких лишних деталей.',
     'prise': '9 149 400₽'},
    {'id': 3, 'title': 'Коттедж «Традиция 1»', 
     'context': 'Коттеджи «Традиция» — шале со вторым светом и большим выбором планировок.',
     'prise': '9 530 200₽'},
]

# Представление 'главной страницы'
def index(request):
    data = {
        'title': 'Главная страница',
        'menu': menu,
        'home': data_db,
        }
    return render(request, 'houses/index.html', data)

# Представление 'страницы про нас'
def about(request):
    data = {
        'title': 'Страница про нас',
        'menu': menu,
        }
    return render(request, 'houses/about.html', context = data)

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
