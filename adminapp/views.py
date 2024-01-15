from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from adminapp import services


def login_required_decorator(func):
    return login_required(func, login_url='login_page')


@ login_required_decorator
def home_page(request):
    faculties = services.get_faculties()
    kafedras = services.get_kafedra()
    return render(request, 'index.html')
