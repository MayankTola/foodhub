from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path(r'', views.menu_global_view, name='MenuGlobal'),
    path(r'form', views.Menu_form, name='MenuForm'),
    path(r'view/', views.menu_view, name='MenuView'),
    path(r'edit/<int:id>', views.menu_edit, name='MenuEdit'),
    path(r'edit/update/<int:id>', views.menu_update, name='MenuUpdate'),
    path(r'delete/<int:id>', views.menu_delete, name='MenuDelete'),
    path(r'order/<int:id>', views.place_order, name='OrderFood'),
    path(r'order-restaurant', views.view_orders_restaurant, name='ViewOrdersRestaurant'),
    path(r'order-customer', views.view_orders_customer, name='ViewOrdersCustomer'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)