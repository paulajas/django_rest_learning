def is_member(user):
    return (
        user.groups.filter(name="group_member").exists()
        or user.groups.filter(name="group_leader").exists()
    )


class BaseReadOnlyAdminMixin:
    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class BaseViewAdminMixin:
    def get_model_perms(self, request):
        if is_member(request.user):
            return {
                "view": True,
            }
        return {
            "view": False,
        }
