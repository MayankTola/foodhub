from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db import transaction
from .models import User, Customer, Restaurant


class CustomerSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)
    location = forms.CharField(required=True)
    food_pref = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_customer = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.food_pref = self.cleaned_data.get('food_pref')
        user.save()
        customer = Customer.objects.create(user=user)
        customer.phone_number = self.cleaned_data.get('phone_number')
        customer.location = self.cleaned_data.get('location')
        customer.food_pref = self.cleaned_data.get('food_pref')
        customer.save()
        return user

    def __init__(self, *args, **kwargs):
        super(CustomerSignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            "name": "username"})
        self.fields['first_name'].widget.attrs.update({
            'class': 'form-control',
            "name": "username"})
        self.fields['last_name'].widget.attrs.update({
            'class': 'form-control',
            "name": "username"})
        self.fields['phone_number'].widget.attrs.update({
            'class': 'form-control',
            "name": "phone_number"})
        self.fields['location'].widget.attrs.update({
            'class': 'form-control',
            "name": "location"})
        self.fields['food_pref'].widget.attrs.update({
            'class': 'form-control',
            "name": "food_pref"})


class RestaurantSignUpForm(UserCreationForm):
    restaurant_name = forms.CharField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)
    designation = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_restaurant = True
        user.is_staff = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        restaurant = Restaurant.objects.create(user=user)
        restaurant.restaurant_name = self.cleaned_data.get('restaurant_name')
        restaurant.phone_number = self.cleaned_data.get('phone_number')
        restaurant.designation = self.cleaned_data.get('designation')
        restaurant.save()
        return user

    def __init__(self, *args, **kwargs):
        super(RestaurantSignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            "name": "username"})
        self.fields['restaurant_name'].widget.attrs.update({
            'class': 'form-control',
            "name": "restaurant_name"})
        self.fields['first_name'].widget.attrs.update({
            'class': 'form-control',
            "name": "username"})
        self.fields['last_name'].widget.attrs.update({
            'class': 'form-control',
            "name": "username"})
        self.fields['phone_number'].widget.attrs.update({
            'class': 'form-control',
            "name": "phone_number"})
        self.fields['designation'].widget.attrs.update({
            'class': 'form-control',
            "name": "designation"})
