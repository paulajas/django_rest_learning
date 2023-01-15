"""tiny URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from cookbook.views import ReceipeAV, CookbookAV, ReceipeCookbookAV, ReceipeNewAV, CookbookNewAV
from cookbook.views import ReceipeDetailAV, CookbookDetailAV, ReceipeCookbookDetailAV, ReceipeCookbookNewAV, ReceipeDetailGetAV

urlpatterns = [
    path("receipe/",ReceipeAV.as_view(),name='receipe-list'),
    # path("receipe/<int:pk>",ReceipeDetailAV.as_view(),name='receipe-detail'),
    path("cookbook/",CookbookAV.as_view(),name='cookbook-list'),
    # path("cookbook/<int:pk>",CookbookDetailAV.as_view(),name='cookbook-detail'),
    path("receipecookbook/", ReceipeCookbookAV.as_view(), name='receipe-cookbook-list'),
    path("receipe/<int:pk>/change/", ReceipeDetailAV.as_view(), name='receipe-detail'),
    path("receipe/<int:pk>/", ReceipeDetailGetAV.as_view(), name='receipe-detail'),
    path("receipe/create", ReceipeNewAV.as_view(), name='receipe-new'),
    path("cookbook/<int:pk>", CookbookDetailAV.as_view(), name='cookbook-detail'),
    path("cookbook/create", CookbookNewAV.as_view(), name='cookbook-new'),
    path("receipecookbook/<int:pk>", ReceipeCookbookDetailAV.as_view(), name='receipe-cookbook-detail'),
    path("receipecookbook/create", ReceipeCookbookNewAV.as_view(), name='receipe-cookbook-new'),
]
