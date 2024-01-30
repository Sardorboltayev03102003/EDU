from django.shortcuts import render

from django.shortcuts import render
from home.models import *


def home_one_popular(request):
    home = HomePopularCourses.objects.all()
    ctx = {
        "home": home,
    }
    return render(request, "index.html", ctx)
# Create your views here.
