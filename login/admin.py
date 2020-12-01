""" Configuracion de administraciónd de usuarios"""

# Django
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin

# Modelos
from django.contrib.auth.models import User
from login.models import Profile,Products

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):

    # Que es lo que quiero que se muestre
    list_display = (
        'name',
        'price',
        'description',
        'img_url',
        'is_active',
        'stock',
        'create_at',
        'update_at'
    )
    # Que elementos son clickables
    list_display_links = ('name',)
    # Que elementos se pueden editar ahi mismo
    list_editable = ( 'price', 'description', 'img_url', 'is_active', 'stock' )
    # list_editable = ('birthdate', 'website', 'picture')
    # Como quieres buscar un elemento
    search_fields = ( 'name', 'price', 'description', 'img_url', 'is_active', 'stock', 'create_at', 'update_at' )
    # Filtro de datos
    # list_filter = ('user__is_active', 'user__is_staff', 'created', 'modified')

class ProductsInline(admin.StackedInline):
    """ Profile in-line admin for users """

    model = Products
    can_delete = False
    verbose_name_plural = 'productos'

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):

    # Que es lo que quiero que se muestre
    list_display = (
        'user',
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


admin.site.unregister(User)
admin.site.register(User)
