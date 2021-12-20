from django.contrib import admin

from .models import Analyst

@admin.register(Analyst)
class AnalystAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'laboratory')


