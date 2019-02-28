from django.db import models

# Create your models here.
class UserModel(models.Model):
    username = models.CharField(max_length=20, default="")
    password = models.CharField(max_length=200, default="")
    age = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.username
