from django.contrib import admin
from .models import Receipe, Cookbook, ReceipeCookbook

# Register your models here.

admin.site.register(Receipe)
admin.site.register(Cookbook)
admin.site.register(ReceipeCookbook) 