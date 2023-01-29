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
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

# import routers from the REST framework
# it is necessary for routing
from rest_framework import routers
from cookbook.views import UserCreate
from cookbook.views import Mainpage
from cookbook.views import ReceipeReactAV
# create a router object
router = routers.DefaultRouter()
# router.register(r'tasks', Receipe, 'task')

router.register(r'receipe', ReceipeReactAV, 'receipie')

urlpatterns = [
    path('', Mainpage.as_view(), name="register"),
    path('admin/', admin.site.urls),
    path('', include('cookbook.urls')),
    path('api/', include(router.urls)),
    path(r'api/users^$', UserCreate.as_view(), name='account-create'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
