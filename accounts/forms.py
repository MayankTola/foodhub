from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db import transaction
from .models import User, Customer, Restaurant

food_choices = (
    ("veg", "veg"),
    ("nonveg", "nonveg"),
)

class CustomerSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    food_pref = forms.ChoiceField(required=True,choices=food_choices)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_customer = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        customer = Customer.objects.create(user=user)
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
        self.fields['food_pref'].widget.attrs.update({
            'class': 'form-control',
            "name": "food_pref"})
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            "name": "password1"})
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            "name": "password2"})

        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''

        self.fields['username'].help_text = ''


class RestaurantSignUpForm(UserCreationForm):
    restaurant_name = forms.CharField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

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
        restaurant.save()
        return user

    def __init__(self, *args, **kwargs):
        super(RestaurantSignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            "name": "username"})
        self.fields['restaurant_name'].widget.attrs.update({
            'class': 'form-control',
            "name": "Restaurant Name"})
        self.fields['first_name'].widget.attrs.update({
            'class': 'form-control',
            "name": "first_name"})
        self.fields['last_name'].widget.attrs.update({
            'class': 'form-control',
            "name": "username"})
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            "name": "password1"})
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            "name": "password2"})

        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''

        self.fields['username'].help_text = ''


User = get_user_model()


class UsersLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput, )

    def __init__(self, *args, **kwargs):
        super(UsersLoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            "name": "username"})
        self.fields['password'].widget.attrs.update({
            'class': 'form-control',
            "name": "password"})

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("Either username or password is incorrect.")
            if not user.check_password(password):
                raise forms.ValidationError("Incorrect Password")
            if not user.is_active:
                raise forms.ValidationError("User is no longer active")

        return super(UsersLoginForm, self).clean(*args, **kwargs)
