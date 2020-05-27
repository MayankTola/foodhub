from django import forms
from .models import *


class HandOver_form(forms.ModelForm):
    class Meta:
        model = menu_details
        fields = "__all__"
        widgets = dict(restaurant_nam=forms.TextInput(attrs={'class': "form-control"}),
                       dish_name=forms.TextInput(attrs={'class': "form-control"}),
                       dish_type=forms.Select(attrs={'class': 'form-control'}),
                       price=forms.TextInput(attrs={'class': "form-control"}),
                       description=forms.Textarea(attrs={'class': "form-control"}))

