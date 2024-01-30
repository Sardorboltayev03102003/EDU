from django.contrib import admin

from base.admin import BaseAdmin
from .models import *


class HomePopularAdmin(BaseAdmin):
    list_display = ('title', 'name', 'image', 'views', 'old_price', 'new_price')


admin.site.register(HomePopularCourses, HomePopularAdmin)
# Register your models here.
