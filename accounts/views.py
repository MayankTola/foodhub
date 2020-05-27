from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect, render
from django.contrib import messages
from django.views.generic import CreateView
from .forms import CustomerSignUpForm, RestaurantSignUpForm, UsersLoginForm
from django.contrib.auth.forms import AuthenticationForm
from .models import User


def register(request):
    return render(request, '../templates/register.html')


class customer_register(CreateView):
    model = User
    form_class = CustomerSignUpForm
    template_name = 'login/login_form.html'
    extra_context = {'title': "Customer Registration"}

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')


class restaurant_register(CreateView):
    model = User
    form_class = RestaurantSignUpForm
    template_name = 'login/login_form.html'
    extra_context = {'title': "Restaurant Registration"}

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')


def login_request(request):
    form = UsersLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect("/")
    return render(request, "login/login_form.html", {
        "form": form, "title": "Log In"
    })


def logout_view(request):
    logout(request)
    return redirect('/')
