from django.db import models

from django.contrib.auth.models import User
from dashboard.models import Card

class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cards = models.ManyToManyField(Card)
    # Atributos
    description = models.TextField(blank=True, null=True)
    birthdate = models.DateField(null=True, )
    cellphone = models.CharField(max_length=10,null=True)
    phone_number = models.CharField(max_length=10,null=True)
    
    TYPE_OF_USER = [
        ('admin','admin'),
        ('medium','medium'),
        ('basic','basic')
    ]

    type_user = models.CharField(max_length=50, choices=TYPE_OF_USER, null=True)

    def __str__(self):

        return str(self.user.username)

class Products(models.Model):
    name = models.CharField(max_length=150,unique=True)
    price = models.IntegerField(default=0)
    description = models.TextField(default="")
    img_url = models.CharField(max_length=150)
    is_active = models.BooleanField(default=True)
    stock = models.IntegerField(default=0)
    create_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.name)

    def sell(self,cantidad):
        self.stock -= cantidad
        return str(self.stock)

    def add(self,cantidad):
        self.stock += cantidad
        return str(self.stock)
