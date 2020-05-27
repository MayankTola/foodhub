from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect, render
from django.contrib import messages
from django.views.generic import CreateView
from .forms import CustomerSignUpForm, RestaurantSignUpForm, UsersLoginForm
from django.contrib.auth.forms import AuthenticationForm
from .models import User


def register(request):
    return render(request, '../templates/register.html')


# def customer_register(request):
#     form = CustomerSignUpForm(request.POST or None)
#     if form.is_valid():
#         user = form.save()
#         password = form.cleaned_data.get("password")
#         user.set_password(password)
#         user.save()
#         new_user = authenticate(username=user.username, password=password)
#         # login(request, new_user)
#         return redirect("/")
#     return render(request, "login/customer_register.html", {
#         "form": form,
#     })
class customer_register(CreateView):
    model = User
    form_class = CustomerSignUpForm
    template_name = 'login/customer_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')


class restaurant_register(CreateView):
    model = User
    form_class = RestaurantSignUpForm
    template_name = 'login/restaurant_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')


# def login_request(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(data=request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect('/')
#             else:
#                 messages.error(request, "Invalid username or password")
#         else:
#             messages.error(request, "Invalid username or password")
#     return render(request, 'login/login_form.html',
#                   context={'form': AuthenticationForm()})

def login_request(request):
    form = UsersLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect("/")
    return render(request, "login/login_form.html", {
        "form": form,
    })


def logout_view(request):
    logout(request)
    return redirect('/')
