from django.shortcuts import render

def index(request):
    data = {
        'title': 'Главная страница'
        }

    return render(request,'handmade_catalog_web/index.html', data)

def about(request):
    return render(request, 'handmade_catalog_web/about.html')
