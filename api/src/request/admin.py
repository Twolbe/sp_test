from django.contrib import admin
from .models import Request 


@admin.register(Request)
class Request(admin.ModelAdmin):
    pass