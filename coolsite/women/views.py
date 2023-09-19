from django.shortcuts import HttpResponse
# для хранения представлений(контроллеры) текущего приложения
# Create your views here.


def index(request):
    return HttpResponse('главная страница women')

def categories(request):
    return HttpResponse('<h1>Статьи по категориям</h1>')

def shrifs(request):
    return HttpResponse('<i>Шрифты</i>')