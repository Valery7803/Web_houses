from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name = 'home'),
    path('about/', views.about, name = 'about'),
    path('contacts/', views.contacts, name = 'contacts'),
    path('<slug:show_id>/', views.show_house, name = 'show_house'),
    path('login/', views.login, name = 'login'),
]