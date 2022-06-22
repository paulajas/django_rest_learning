from django.contrib import admin

class MeatReceipeAdmin(admin.ModelAdmin):
    filter_horizontal = ['cookbook']