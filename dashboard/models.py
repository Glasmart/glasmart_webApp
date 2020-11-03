from django.db import models

# Modelos
from django.contrib.auth.models import User
from login.models import Profile, UserProfile

class Card(models.Model):

    # Atributos
    name        = models.TextField(null=False, default='')
    iconClass   = models.TextField(null=False, default='')
    direction   = models.TextField(null=False, default='')
    active      = models.BooleanField(default=True)
    create_at   = models.DateField(auto_now_add=True)
    update_at   = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.name)

    def toggleActive(self):
        self.active = not self.active
        self.save()

        return "Cambio Hecho!"

class UserCard(models.Model):

    # Atributos
    user        = models.ForeignKey(User, on_delete=models.CASCADE)
    card        = models.ForeignKey(Card, on_delete=models.CASCADE)
    profile     = models.ForeignKey(Profile, on_delete=models.CASCADE)
    active      = models.BooleanField(default=True)
    create_at   = models.DateField(auto_now_add=True)
    update_at   = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.name)

    def toggleActive(self):
        self.active = not self.active
        self.save()

        return "Cambio Hecho!"
