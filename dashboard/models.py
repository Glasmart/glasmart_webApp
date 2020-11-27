from django.db import models


class Card(models.Model):

    # Atributos
    name = models.CharField(max_length=150,unique=True)
    iconClass = models.CharField(max_length=150)
    url = models.CharField(max_length=80,unique=True)
    is_active = models.BooleanField(default=True)
    create_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.name)

    def toggleActivo(self):
        self.is_active = not self.is_active
        return str(self.is_active)
