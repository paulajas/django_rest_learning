from django.contrib import admin
from guardian.admin import GuardedModelAdmin
from guardian.shortcuts import get_objects_for_user
from receipe.models import CookBookReceipe

from receipe.models import CookBook

class CookBookReceipeInLine(admin.TabularInline):
        model=CookBookReceipe

class CookBookAdmin(GuardedModelAdmin):
    list_display = ("name",)
    search_fields = ['name',]
    exclude = ['user',]

    def get_search_results(self, request, queryset, search_term):

        """
        Make list of cookbook from cached in db queryset or
        running queryset for new disease.
        """
        print("lol")
        setattr(self, "user", request.user)
        if search_term == "":
            print("to tu")
            queryset = CookBook.objects.filter(public=True)
            print(queryset)
            queryset_2  = get_objects_for_user(self.user, "view_cookbook", klass=CookBook)
            queryset = queryset | queryset_2
            print(get_objects_for_user(self.user, "view_cookbook", klass=CookBook))
        else:
            queryset  = get_objects_for_user(self.user, "view_cookbook", klass=CookBook).filter(name__icontains=search_term)
        return (queryset, True)

    def save_new(self, request, obj, form, change):
        obj.user = request.user
        super().save_new(request, obj, form, change)

    inlines = (CookBookReceipeInLine,)

    