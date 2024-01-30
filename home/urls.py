from django.urls import path

from .views import *

urlpatterns = [
    path('', home_one_popular, name='index')
    ]