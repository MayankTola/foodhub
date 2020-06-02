from django import forms
from .models import *
from django.conf import settings


class menu_form(forms.ModelForm):
    class Meta:
        model = menu_details
        exclude = ('restaurant',)
        fields = "__all__"
        widgets = dict(dish_name=forms.TextInput(attrs={'class': "form-control"}),
                       dish_type=forms.Select(attrs={'class': 'form-control'}),
                       price=forms.TextInput(attrs={'class': "form-control"}),
                       description=forms.Textarea(attrs={'class': "form-control"}))




class order_form(forms.ModelForm):
    class Meta:
        model = order_details
        fields = "__all__"

