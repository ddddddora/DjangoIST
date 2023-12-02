from django.db import models

Students = [
    {'id' : 1, 'FI' : 'Буренок Дмитрий', "gender" : 'm', 'is_smoke' : True, 'birthday' : '14.01.2005'},
    {'id' : 2, 'FI' : 'Горбанев Кирилл', "gender" : 'm', 'is_smoke' : False, 'birthday' : '25.01.2006'},
    {'id' : 3, 'FI' : 'Капшукова Дарья', "gender" : 'f', 'is_smoke' : False, 'birthday' : '27.06.2004'},
    {'id' : 4, 'FI' : 'Кашаева Раяна', "gender" : 'f', 'is_smoke' : False, 'birthday' : '27.06.2004'},
    {'id' : 5, 'FI' : 'Климин Тимур', "gender" : 'm', 'is_smoke' : False, 'birthday' : '17.05.2004'},
    {'id' : 6, 'FI' : 'Косенков Глеб', "gender" : 'm', 'is_smoke' : False, 'birthday' : '9.06.2004'},
    {'id' : 7, 'FI' : 'Костин Максим', "gender" : 'm', 'is_smoke' : False, 'birthday' : '3.04.2001'},
    {'id' : 8, 'FI' : 'Кузенков Богдан', "gender" : 'm', 'is_smoke' : True, 'birthday' : ''},
    {'id' : 9, 'FI' : 'Миколадзе Антон', "gender" : 'm', 'is_smoke' : True, 'birthday' : '14.09.2004'},
    {'id' : 10, 'FI': 'Мишин Александр', "gender" : 'm', 'is_smoke' : False, 'birthday' : '21.08.2004'},
    {'id' : 11, 'FI': 'Мишин Алексей', "gender" : 'm', 'is_smoke' : False, 'birthday' : '21.08.2004'},
    {'id' : 12, 'FI': 'Пешеходько Арсений', "gender" : 'm', 'is_smoke' : True, 'birthday' : '10.11.2004'},
    {'id' : 13, 'FI' : 'Сентюрина Екатерина', "gender" : 'f', 'is_smoke' : False, 'birthday' : '8.11.2002'}]

class Student(models.Model):
    FI = models.CharField(max_length=30)
    gender = models.CharField(max_length=30)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_smoke = models.BooleanField(default=False)
    birthday = models.DateTimeField(auto_now=True)

base_book = [
    {'id': 1, 'name': 'Великий Гэтсби', 'price': 200, 'publication': 'Эксмо', 'author': 'Фрэнсис Скотт Фицджеральд'},
    {'id': 2, 'name': 'Унесенные ветром', 'price': 257, 'publication': 'Эксмо', 'author': 'Маргарет Митчелл'},
    {'id': 3, 'name': 'Повесть о двух городах', 'price': 150, 'publication': 'Эксмо', 'author': 'Чарлз Диккенс'},
    {'id': 4, 'name': 'Ромео и Джульетта', 'price': 325, 'publication': 'Эксмо', 'author': 'Уильям Шекспир'},
    {'id': 5, 'name': 'Жизнь Пи', 'price': 427, 'publication': 'Эксмо', 'author': 'Янн Мартел'},
]

class Book(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField()
    publication = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    slug = models.SlugField(max_length=255, db_index=True, unique=True, verbose_name="URL")

    def __str__(self):
        return self.name

    def __str__(self):
        return self.name