from django.contrib import admin
from django.contrib.admin import AdminSite
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
# physician_interface_admin_site.register(Patient, PatientAdmin)


