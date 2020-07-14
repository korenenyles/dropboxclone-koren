
# from django.contrib import admin
# from django.contrib.auth import UserAdmin
# from dropbox_user.models import DropBoxUser, DropBoxUserManager
# from dropbox_user.forms import RegisterForm, UserAdminCreationForm, UserAdminChangeForm

# class DropBoxUserAdminForm(UserAdmin):
#     form = UserAdminChangeForm
#     add_form = UserAdminCreationForm

from django.contrib import admin
from .models import DropBoxUser
from django.contrib.auth.admin import UserAdmin

# https://www.youtube.com/
# watch?v=XJU9vRARkGo&list=PLgCYzUzKIBE_dil025VAJnDjNZHHHR9mW&index=13


class DropBoxUserAdmin(UserAdmin):
    list_display = ('email', 'display_name', 'created_at',
                    'is_active', 'is_staff', 'is_admin')
    search_fields = ('email', 'display_name')
    readonly_fields = ('created_at', 'is_active')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(DropBoxUser, DropBoxUserAdmin)


# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from .models import DropBoxUser, DropBoxUserManager
# # from dropbox_user.forms import RegisterForm, UserAdminCreationForm


# class DropBoxUserAdminForm(UserAdmin):
#     # form = UserAdminChangeForm
#     # add_form = UserAdminCreationForm


#     list_display = ('email', 'admin')
#     list_filter = ('admin', 'staff', 'active')
#     field_sets = (
#         (None, {'fields': ('email', 'password')}),
#         ('personal info', {'fields': ('display_name',)}),
#         ('permissions', {'fields': ('admin', 'staff', 'active_user')})
#     ),

#     add_fieldsets = (
#         (None, {
#             'classes': ('wide'),
#             'fields': ('emails', 'password1', 'password2')
#         })
#     )

#     admin.site.register(DropBoxUser)

#     admin.site.register(DropBoxUserManager)

#     admin.site.register(DropBoxUserManager)
