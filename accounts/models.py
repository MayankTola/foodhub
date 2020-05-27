from django.db import models
from django.contrib.auth.models import AbstractUser

food_choices = (
    ("veg", "veg"),
    ("nonveg", "nonveg"),
)


class User(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_restaurant = models.BooleanField(default=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    phone_number = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    food_pref = models.CharField(max_length=10, default='veg')


class Restaurant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    restaurant_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    designation = models.CharField(max_length=20)
