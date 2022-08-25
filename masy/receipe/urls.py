from django.contrib import admin
from django.urls import include, path
from receipe.views import country_list, country_detail, picture_list
from receipe.admin.admin import receipe_interface_admin_site
from receipe.views import register

urlpatterns = [
    path('admin/', admin.site.urls),
    path("receipe/", receipe_interface_admin_site.urls),
    path("", register, name="register"),
    path('api-auth/', include('rest_framework.urls')),
    # path('country/', country_list, name='country-list'),
    # path('<int:pk>', country_detail, name='country-detail'),
    path('picture/', picture_list, name="picture-list")
]
