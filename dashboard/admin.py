""" Configuracion de administraciónd de usuarios"""

# Django
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin

# Modelos
from django.contrib.auth.models import User
from login.models import Profile, UserProfile
from dashboard.models import Card, UserCard

@admin.register(Card)
class CardAdmin(admin.ModelAdmin):

    # Que es lo que quiero que se muestre
    list_display = (
        'name',
        'direction',
        'iconClass',
    )
    # Que elementos son clickables
    list_display_links = ('name',)
    # Que elementos se pueden editar ahi mismo
    list_editable = ('iconClass', 'direction')
    # Como quieres buscar un elemento
    search_fields = ('name', )
    # Filtro de datos
    # list_filter = ('user__is_active', 'user__is_staff', 'created', 'modified')

class CardInline(admin.StackedInline):
    """ Profile in-line admin for users """

    model = Card
    can_delete = False
    verbose_name_plural = 'cards'


@admin.register(UserCard)
class UserCardAdmin(admin.ModelAdmin):

    # Que es lo que quiero que se muestre
    list_display = (
        'user',
        'card',
        'profile',
        'active',
        'create_at',
        'update_at',
    )
    # Que elementos son clickables
    list_display_links = ('user',)
    # Que elementos se pueden editar ahi mismo
    # list_editable = ('birthdate', 'website', 'picture')
    # Como quieres buscar un elemento
    search_fields = ('user__username', 'profile__name', 'created_at', 'update_at')
    # Filtro de datos
    # list_filter = ('user__is_active', 'user__is_staff', 'created', 'modified')

class UserCardline(admin.StackedInline):
    """ Profile in-line admin for users """

    model = UserCard
    can_delete = False
    verbose_name_plural = 'usercards'





