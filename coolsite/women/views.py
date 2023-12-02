from django.core.exceptions import BadRequest
from django.http import HttpResponseNotFound, HttpResponseForbidden, HttpResponseServerError, HttpResponseBadRequest
from django.shortcuts import render, redirect, get_object_or_404

from women.models import Book

treatment = [
    {'kod': 243, 'disease': 'Грипп', 'dosage': '500 mg'},
    {'kod': 56,'disease': 'Авитаминоз', 'dosage': '10 mg'},
    {'kod': 23,'disease': 'Аллергические заболевания', 'dosage': '1,8 mg'},
    {'kod': 575,'disease': 'Ринит', 'dosage': '564 mg'},
    {'kod': 234,'disease': 'Гайморит', 'dosage': '40 mg'},
    {'kod': 675,'disease': 'Панкреатит', 'dosage': '200 mg'},
]

Students = [
    {'id' : 1, 'FI' : 'Буренок Дмитрий', "gender" : 'm', 'is_smoke' : True, 'birthday' : '14.01.2005','image_': 'dima.jpg'},
    {'id' : 2, 'FI' : 'Горбанев Кирилл', "gender" : 'm', 'is_smoke' : False, 'birthday' : '25.01.2006','image_': 'kirill.png'},
    {'id' : 3, 'FI' : 'Капшукова Дарья', "gender" : 'f', 'is_smoke' : False, 'birthday' : '27.06.2004','image_': 'i am.jpg'},
    {'id' : 4, 'FI' : 'Кашаева Раяна', "gender" : 'f', 'is_smoke' : False, 'birthday' : '27.06.2004','image_': 'rayana.jpg'},
    {'id' : 5, 'FI' : 'Климин Тимур', "gender" : 'm', 'is_smoke' : False, 'birthday' : '17.05.2004','image_': 'tim.jpg'},
    {'id' : 6, 'FI' : 'Косенков Глеб', "gender" : 'm', 'is_smoke' : False, 'birthday' : '9.06.2004','image_': 'gleb.jpg'},
    {'id' : 7, 'FI' : 'Костин Максим', "gender" : 'm', 'is_smoke' : False, 'birthday' : '3.04.2001','image_': 'maxim.jpg'},
    {'id' : 8, 'FI' : 'Кузенков Богдан', "gender" : 'm', 'is_smoke' : True, 'birthday' : '','image_': 'bogdan.jpg'},
    {'id' : 9, 'FI' : 'Миколадзе Антон', "gender" : 'm', 'is_smoke' : True, 'birthday' : '14.09.2004','image_': 'anton.jpg'},
    {'id' : 10, 'FI': 'Мишин Александр', "gender" : 'm', 'is_smoke' : False, 'birthday' : '21.08.2004','image_': 'sasha.jpg'},
    {'id' : 11, 'FI': 'Мишин Алексей', "gender" : 'm', 'is_smoke' : False, 'birthday' : '21.08.2004','image_': 'lesha.jpg'},
    {'id' : 12, 'FI': 'Пешеходько Арсений', "gender" : 'm', 'is_smoke' : True, 'birthday' : '10.11.2004','image_': 'senya.jpg'},
    {'id' : 13, 'FI' : 'Сентюрина Екатерина', "gender" : 'f', 'is_smoke' : False, 'birthday' : '8.11.2002','image_': 'kate.jpg'}]


base_book = [
    {'id': 1, 'name': 'Великий Гэтсби', 'price': 200, 'publication': 'Эксмо', 'author': 'Фрэнсис Скотт Фицджеральд'},
    {'id': 2, 'name': 'Унесенные ветром', 'price': 257, 'publication': 'Эксмо', 'author': 'Маргарет Митчелл'},
    {'id': 3, 'name': 'Повесть о двух городах', 'price': 150, 'publication': 'Эксмо', 'author': 'Чарлз Диккенс'},
    {'id': 4, 'name': 'Ромео и Джульетта', 'price': 325, 'publication': 'Эксмо', 'author': 'Уильям Шекспир'},
    {'id': 5, 'name': 'Жизнь Пи', 'price': 427, 'publication': 'Эксмо', 'author': 'Янн Мартел'},
]

menu = [
    {'title': 'Главная страница', 'url_n': 'home'},
    {'title': 'О приложении', 'url_n': 'about'},
    {'title': 'Студенты', 'url_n': 'surn'},
    {'title': 'Аптека', 'url_n': 'apteka'},
]

data = {'students': Students, 'menu': menu, 'student_url': 'students_id',}
def index(request):
    return render(request, 'women/index.html', context=data)
def about(request):
    return render(request, 'women/about.html', context=data)
def apteka(request):
    return render(request, 'women/apteka.html', context=data)


def student_index(request, student_id):
    if 1 <= student_id <= 13:
        current = Students[student_id - 1]
        return render(request, 'women/current_student.html', context=current)

def book(request, book_name):
    base_book = get_object_or_404(Book, slug= book_name)
    data = {'title': 'Главная страница',
            'book': base_book,
            'menu': menu,
            }
    return render(request, 'women/book.html', context=data)


def Students_mainpage(request):
    return render(request, 'women/sername.html', context=data)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
def Forbidden(request, exception):
    return HttpResponseForbidden('<h1>Доступ запрещён</h1>')
def InternalServerError(request):
    return HttpResponseServerError('<h1>Ошибка сервера</h1>')
def ErrBadRequest(request, exception):
    return HttpResponseBadRequest('<h1>Неверный запрос</h1>')
def err_400(request):
    raise BadRequest
def err_500(request):
    raise ffff
# имитация ошибки сервера