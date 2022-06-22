from django.contrib import admin
from django.contrib.admin import AdminSite
from receipe.models import BreakfastReceipe, DinnerReceipe, LunchReceipe, SnackReceipe, VegeReceipe
from receipe.models import CookBook
from receipe.admin.CookBook import CookBookAdmin
from receipe.models import Country
from receipe.models import MeatReceipe
from receipe.admin.permission import BaseViewAdminMixin




admin.site.site_header = "Receipe Interface"

class ReceipeAdminSite(BaseViewAdminMixin, AdminSite): # wielodziedziczenie
    site_header = "Receipe Interface"

    def get_model_perms(self, request):
        if request.user.username == "receipe_interface":
            return {
                "view": True,
            }
        return {
            "view": False,
        }


receipe_interface_admin_site = ReceipeAdminSite(
    name="receipe_interface_admin_site"
)
receipe_interface_admin_site.register(MeatReceipe)
receipe_interface_admin_site.register(Country)
receipe_interface_admin_site.register(CookBook, CookBookAdmin)
receipe_interface_admin_site.register(VegeReceipe)
receipe_interface_admin_site.register(BreakfastReceipe)
receipe_interface_admin_site.register(LunchReceipe)
receipe_interface_admin_site.register(DinnerReceipe)
receipe_interface_admin_site.register(SnackReceipe)
