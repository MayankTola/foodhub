import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import *
from .models import *


@login_required()
def Menu_form(request):
    form = menu_form()  # form called from forms.py
    if request.method == "POST":
        form = menu_form(request.POST or None, request.FILES)
        if form.is_valid():
            menu = form.save(commit=False)
            menu.restaurant_name = request.user
            menu.save()
            return redirect("/")
        else:
            print(form.errors)
    return render(request, "menu/menu_form.html", {"form": form})


@login_required()
def menu_view(request):
    # content = menu_details.objects.all()
    content = menu_details.objects.filter(restaurant_name=request.user)
    return render(request, "menu/menu_view.html", {'content': content})


@login_required()
def menu_edit(request, id):
    content = menu_details.objects.get(id=id)
    form = menu_form(request.POST or None, instance=content)
    return render(request, 'menu/menu_update.html', {'form': form, 'content': content})


@login_required()
def menu_update(request, id):
    content = menu_details.objects.get(id=id)
    form = menu_form(request.POST or None, request.FILES, instance=content)
    if form.is_valid():
        form.save()
        return redirect("/menu/view/")
    else:
        print(form.errors)
    return render(request, 'menu/menu_update.html', {'form': form, 'content': content})


@login_required()
def menu_delete(request, id):
    content = menu_details.objects.get(id=id)
    content.delete()
    return redirect("/menu/view/")


def menu_global_view(request):
    pr=request.user.customer.food_pref
    print(pr)
    content = menu_details.objects.all()
    return render(request, "menu/order_view.html", {'content': content})


@login_required()
def order_placed(request, id):
    content = menu_details.objects.get(id=id)
    menu_content = menu_details.objects.all()
    cust_name = request.user.username
    r_name = content.restaurant_name
    dish_name = content.dish_name
    dish_type = content.dish_type
    price = content.price
    description = content.description

    data = order_details(customer_name=cust_name, restaurant_name=r_name, description=description,
                         dish_name=dish_name, dish_type=dish_type, price=price)
    data.save()
    return render(request, 'menu/order_view.html', {'content': menu_content})


@login_required()
def view_orders(request):
    content = order_details.objects.filter(restaurant_name=request.user)
    return render(request, "order/order_view.html", {'content': content})
