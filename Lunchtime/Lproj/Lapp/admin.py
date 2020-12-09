from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import MyUser


# So, is this all setting up a regular user or an admin? Should that be spread amongst the two files?
# can it be in a reasonable way, and what bits are needed for that? what about groups? ughhhhhh
# Unregister the provided model admin
# admin.site.unregister(MyUser)

# Register our own model admin, based on the default UserAdmin
@admin.register(MyUser)
class CustomUserAdmin(UserAdmin):
    readonly_fields = [
        'date_joined',
    ]

    actions = [
        'activate_users',
    ]

    # means a superuser has the ability to batch activate users
    def activate_users(self, request, queryset):
        assert request.user.has_perm('auth.change_user')
        cnt = queryset.filter(is_active=False).update(is_active=True)
        self.message_user(request, 'Activated {} users.'.format(cnt))

    activate_users.short_description = 'Activate Users'  # type: ignore

    def get_actions(self, request):
        actions = super().get_actions(request)
        if not request.user.has_perm('auth.change_user'):
            del actions['activate_users']
        return actions

    def get_form(self, request, obj=None, **kwargs):
        pass
