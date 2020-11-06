from django.db import models

from django.contrib.auth.models import User
from dashboard.models import Card

class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cards = models.ManyToManyField(Card)
    # Atributos
    description = models.TextField(blank=True, null=True)
    birthdate = models.TextField(null=True)
    cellphone = models.TextField(null=True)
    phone_number = models.TextField(null=True)
    
    TYPE_OF_USER = [('admin','admin'),
                    ('medium','medium'),
                    ('basic','basic')
                    ]

    type_user = models.CharField(max_length=255, choices=TYPE_OF_USER, null=True)

    def __str__(self):

        return str(self.user.username)

