from django.db import models

# Modelos
from django.contrib.auth.models import User
from login.models import Profile, UserProfile

class Card(models.Model):

    # Atributos
    name        = models.TextField(null=False)
    direction   = models.TextField(null=False)
    id_profile  = models.ManyToOneRel(Profile,on_delete=models.CASCADE)
    active      = models.BooleanField(default=Tue)
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
    id_user     = models.ManyToOneRel(User, on_delete=models.CASCADE)
    id_profile  = models.ManyToOneRel(Profile, on_delete=models.CASCADE)
    active      = models.BooleanField(default=Tue)
    create_at   = models.DateField(auto_now_add=True)
    update_at   = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.name)

    def toggleActive(self):
        self.active = not self.active
        self.save()

        return "Cambio Hecho!"
