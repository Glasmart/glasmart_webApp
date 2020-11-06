""" Configuracion de administraciónd de usuarios"""

# Django
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin

# Modelos
from django.contrib.auth.models import User
from login.models import Profile
from dashboard.models import Card

@admin.register(Card)
class CardAdmin(admin.ModelAdmin):

    # Que es lo que quiero que se muestre
    list_display = (
        'name',
        'url',
        'iconClass',
    )
    # Que elementos son clickables
    list_display_links = ('name',)
    # Que elementos se pueden editar ahi mismo
    list_editable = ('iconClass', 'url')
    # Como quieres buscar un elemento
    search_fields = ('name', )
    # Filtro de datos
    # list_filter = ('user__is_active', 'user__is_staff', 'created', 'modified')

class CardInline(admin.StackedInline):
    """ Profile in-line admin for users """

    model = Card
    can_delete = False
    verbose_name_plural = 'cards'







