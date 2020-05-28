from django import forms
from .models import *
from django.conf import settings


class menu_form(forms.ModelForm):
    class Meta:
        model = menu_details
        exclude = ('restaurant_name',)
        fields = "__all__"
        widgets = dict(dish_name=forms.TextInput(attrs={'class': "form-control"}),
                       dish_type=forms.Select(attrs={'class': 'form-control'}),
                       price=forms.TextInput(attrs={'class': "form-control"}),
                       description=forms.Textarea(attrs={'class': "form-control"}))

    # def save(self, commit=True):
    #     self.instance.restaurant_name = self.request.user
    #     return super().save(commit=commit)
