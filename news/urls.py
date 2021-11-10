from django.urls import path
from . import views

urlpatterns = [ #отслеживание url адресов
    path('', views.news_home, name='news_home'),
    path('create', views.create, name='create')
]
