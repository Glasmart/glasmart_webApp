from django.db import models


class Card(models.Model):

    # Atributos
    name = models.TextField(null=False, default='')
    iconClass = models.TextField(null=False, default='')
    url = models.URLField(null=False, default='')
    is_active = models.BooleanField(default=True)
    create_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.name)


