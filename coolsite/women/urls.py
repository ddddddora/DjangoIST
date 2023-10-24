from DjangoIST.coolsite.women.classurl import FourDigitYearConverter
from django.urls import path, register_converter

from . import views

register_converter(FourDigitYearConverter, "yyyy")

urlpatterns = [

    path('', views.index),
    path('Students/', views.help),
    path('Students/<int:student_id>/', views.student_index),
    path('years/<yyyy:year_id>/', views.year),
    path('years/', views.years_mainpage),
    path('client_err_test/', views.err_400),
    path('server_err_test/', views.err_500),
    path('alphabet/<yyyy:symbol>', views.display_char),
    path("archive/<yyyy:year>", views.archive),
]
