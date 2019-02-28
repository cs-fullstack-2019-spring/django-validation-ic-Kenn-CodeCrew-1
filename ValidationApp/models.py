from django.db import models

# Create your models here.
class UserModel(models.Model):
    username = models.CharField(max_length=20, default="")
    password = models.CharField(max_length=200, default="")
    age = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.username


class CocktailModel(models.Model):
    name = models.CharField(max_length=500, default="")
    alcoholContent = models.DecimalField(decimal_places=3, max_digits=6, default=0.0)
    servingContainer = models.CharField(max_length=50, default="")
