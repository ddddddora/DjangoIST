from DjangoIST.coolsite.women.classurl import FourDigitYearConverter
from django.urls import path, register_converter

from . import views

register_converter(FourDigitYearConverter, "yyyy")

urlpatterns = [

    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('student/', views.Students, name='surn'),
    path('apteka/', views.apteka, name='apteka'),
    path('Students/<int:student_id>/', views.student_index, name='students_id'),
    path('years/<yyyy:year_id>/', views.year, name='years_id'),
    path('years/', views.years_mainpage, name='years'),
    path('client_err_test/', views.err_400),
    path('server_err_test/', views.err_500),
    path('alphabet/<yyyy:symbol>', views.display_char, name='alphabet'),
    path("archive/<yyyy:year>", views.archive, name='archive'),
]
