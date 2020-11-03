from django.db import models

from django.contrib.auth.models import User

class Profile(models.Model):

    # Atributos
    name        = models.TextField(null=False)
    description = models.TextField(blank=True, null=True)
    active      = models.BooleanField(default=True)
    create_at   = models.DateField(auto_now_add=True)
    update_at   = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.name)

    def toggleActive(self):
        self.active = not self.active
        self.save()

        return "Cambio Hecho!"

class UserProfile(models.Model):

    # Atributos

    id_profile  = models.ForeignKey(Profile,on_delete=models.CASCADE)
    id_user     = models.OneToOneField(User,on_delete=models.CASCADE)
    active      = models.BooleanField(default=True)
    create_at   = models.DateField(auto_now_add=True)
    update_at   = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.id_profile.name+"-"+self.id_user.username)

    def toggleActive(self):
        self.active = not self.active
        self.save()

        return "Cambio Hecho!"