""" Configuracion de administraciónd de usuarios"""

# Django
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin

# Modelos
from django.contrib.auth.models import User
from login.models import Profile

# @admin.register(UserProfile)
# class UserProfileAdmin(admin.ModelAdmin):

#     # Que es lo que quiero que se muestre
#     list_display = (
#         'id_profile', 
#         'id_user',
#         'active',
#         'create_at',
#         'update_at',
#     )
#     # Que elementos son clickables
#     list_display_links = ('id_user',)
#     # Que elementos se pueden editar ahi mismo
#     # list_editable = ('birthdate', 'website', 'picture')
#     # Como quieres buscar un elemento
#     search_fields = ('user__first_name', 'user__username', 'created_at', 'update_at')
#     # Filtro de datos
#     # list_filter = ('user__is_active', 'user__is_staff', 'created', 'modified')

# class ProfileInline(admin.StackedInline):
#     """ Profile in-line admin for users """

#     model = Profile
#     can_delete = False
#     verbose_name_plural = 'profiles'

# class UserAdmin(BaseUserAdmin):
#     """ Add profile admin to base user admin """

#     inlines = (ProfileInline,)
#     list_display = (
#         'username',
#         'email',
#         'first_name',
#         'last_name',
#         'is_active',
#         'is_staff'
#     )
#     list_editable=('is_active', 'is_staff')

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):

    # Que es lo que quiero que se muestre
    list_display = (
        'description',
    )
    # Que elementos son clickables
    # list_display_links = ('name',)
    # Que elementos se pueden editar ahi mismo
    # list_editable = ('birthdate', 'website', 'picture')
    # Como quieres buscar un elemento
    search_fields = ('descripion',)
    # Filtro de datos
    # list_filter = ('user__is_active', 'user__is_staff', 'created', 'modified')

class ProfileInline(admin.StackedInline):
    """ Profile in-line admin for users """

    model = Profile
    can_delete = False
    verbose_name_plural = 'profiles'

# class ProfileAdmin(BaseUserAdmin):
#     """ Add profile admin to base user admin """

#     inlines = (Profile,)
#     list_display = (
#         'name',
#         'description',
#     )
#     #list_editable=('is_active', 'is_staff')



admin.site.unregister(User)
admin.site.register(User)
