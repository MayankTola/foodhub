from django.urls import path
from . import views

urlpatterns = [
    # path(r'add_item/', views.add_item, name='register'),
    path(r'', views.Menu_form, name='MenuForm'),
    path(r'delete/<int:id>', views.menu_delete, name='MenuDelete'),
    path(r'view/', views.menu_view, name='MenuView'),
    path(r'edit/<int:id>', views.menu_edit, name='MenuEdit'),
    path(r'edit/update/<int:id>', views.menu_update, name='MenuUpdate'),
]
