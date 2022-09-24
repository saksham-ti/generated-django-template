from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass
    # add additional fields in here

    def __str__(self):
        return self.username


class UserAddress(models.Model):
    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE)
    building = models.CharField(max_length=128)
    street_1 = models.CharField(max_length=128)
    street_2 = models.CharField(max_length=128)
    city = models.CharField(max_length=128)
    state = models.CharField(max_length=128)
    country = models.CharField(max_length=128)