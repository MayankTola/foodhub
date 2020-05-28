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
            rest = form.save(commit=False)
            rest.restaurant_name = request.user
            rest.save()
            return redirect("/")
        else:
            print(form.errors)
    return render(request, "menu/menu_form.html", {"form": form})


@login_required()
def menu_view(request):
    # content = menu_details.objects.all()
    content = menu_details.objects.filter(restaurant_name=request.user)
    print(request.user)
    return render(request, "menu/menu_view.html", {'content': content})


@login_required()
def menu_edit(request, id):
    content = menu_details.objects.get(id=id)
    form = menu_form(request.POST or None, instance=content)

    return render(request, 'menu/menu_update.html', {'form': form, 'content': content})
#
#
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
