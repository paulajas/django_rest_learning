"""masy URL Configuration

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
from django.urls import include, path
from receipe.views import CityAV
from receipe.views import TagAV
from receipe.views import CountryAV, CountryDetailAV
# from receipe.views import cookbook_list
from receipe.admin.admin import receipe_interface_admin_site
from receipe.views import register
from receipe.views import picture_list
# from receipe.views import country_list, country_detail,

urlpatterns = [
    path('admin/', admin.site.urls),
    path("receipe/", receipe_interface_admin_site.urls),
    path("", register, name="register"),
    path('api-auth/', include('rest_framework.urls')),
    # path('country/', country_list, name='country-list'),
    # path('country/<int:pk>', country_detail, name='country-detail'),
    path('picture/', picture_list, name="picture-list"),
    # path('cookbook/', cookbook_list, name='cookbooks')
    path('country/', CountryAV.as_view(), name='country-list-detail'),
    path('city/', CityAV.as_view(), name='city-list-detail'),
    path("country/<int:pk>", CountryDetailAV.as_view(), name='country-detail'),
    path('tag/', TagAV.as_view(), name='tag-list'),
    
]
