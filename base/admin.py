from django.contrib import admin


class BaseAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'update_at')

# Register your models here.
