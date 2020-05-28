from django.contrib.auth import get_user_model
from django.db import models
from django.http import request
from accounts.forms import User
from django.conf import settings

food_type = (
    ("veg", "veg"),
    ("nonveg", "nonveg"),
)
# name = (('name', User.get_username),)


class menu_details(models.Model):
    restaurant_name = models.CharField(max_length=100, default='none')
    # restaurant_name = models.ForeignKey(User, help_text="", blank=True, null=True, on_delete=models.CASCADE)
    dish_name = models.CharField(blank=False, max_length=20)
    dish_type = models.CharField(max_length=10, choices=food_type, default='veg')
    price = models.CharField(blank=True, max_length=20)
    description = models.TextField(blank=True, max_length=5000)
    image = models.ImageField(blank=True)

    class Meta:
        db_table = "menu_details"
