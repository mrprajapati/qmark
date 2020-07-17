from django.contrib import admin
from accounts.models import Account
from django.contrib.auth.admin import UserAdmin


class AccountAdmin(UserAdmin):
    list_display = ('name', 'email', 'date_joined',
                    'last_login', 'is_admin', 'is_staff')
    search_fields = ('name', 'email',)
    readonly_fields = ('date_joined', 'last_login',)

    filter_horizontal = ("user_permissions", "groups")
    list_filter = ('is_active', 'is_staff', 'is_admin',)
    fieldsets = (
        (None, {'fields': ('email', 'name', 'is_active', 'password')}),
        ('Permissions', {
            'fields': ('is_staff', 'is_superuser', 'is_admin', 'groups', 'user_permissions'),
        }),
        ('Other', {
            'fields': ('last_login', 'date_joined'),
        }),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'password1', 'password2'),
        }),
    )
    ordering = ('name',)
    # exclude = ('username',)

    # def get_actions(self, request):
    #     actions = super().get_actions(request)
    #     # if 'delete_selected' in actions:
    #     #     del actions['delete_selected']
    #     return actions


admin.site.register(Account, AccountAdmin)
# admin.site.register(Group)
