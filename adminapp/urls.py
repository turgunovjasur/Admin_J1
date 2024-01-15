from django.urls import path
from .views import *


urlpatterns = [
    path('', home_page, name='home_page'),                   # hech narsa bosilmasa, 'home_page'ga o'tilsin
    path('login_page/', login_page, name='login_page'),
    path('logout_page/', logout_page, name='logout_page'),
]