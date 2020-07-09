from django.contrib import admin
from django.contrib.auth import UserAdmin
from dropbox_user.models import DropBoxUser, DropBoxUserManager
from dropbox_user.forms import RegisterForm, UserAdminCreationForm, UserAdminChangeForm

class DropBoxUserAdminForm(UserAdmin):
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    list_display = ('email', 'admin')
    list_filter = ('admin', 'staff', 'active')
    field_sets = (
        (None, {'fields': ('email', 'password')}),
        ('personal info', {'fields': ('display_name',)}),
        ('permissions', {'fields': ('admin', 'staff', 'active_user')})
    ),

    add_fieldsets = (
        (None, {
            'classes': ('wide'),
            'fields': ('emails', 'password1', 'password2')
        })
    )

    admin.site.register(DropBoxUser)
    admin.site.register(DropBoxUserManager)