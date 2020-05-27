from django.db import models
from datetime import datetime


food_type = (
    ("veg", "VEG"),
    ("nonveg", "Non VEG"),
)


# Create your models here.
class menu_details(models.Model):
    restaurant_name = models.CharField(blank=True, max_length=20)
    dish_name = models.CharField(blank=True, max_length=20)
    dish_type = models.CharField(max_length=10, choices=food_type, default='veg')
    price = models.CharField(blank=True, max_length=20)
    description = models.TextField(blank=True, max_length=5000)
    image = models.ImageField0(blank=True)

    class Meta:
        db_table = "menu_details"
