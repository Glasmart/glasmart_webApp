from django.db import models


class Card(models.Model):

    # Atributos
    name = models.CharField(max_length=150,unique=True)
    iconClass = models.CharField(max_length=150)
    url = models.URLField(null=False, default='')
    is_active = models.BooleanField(default=True)
    create_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.name)


