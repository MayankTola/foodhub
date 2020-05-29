from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path(r'', views.Menu_form, name='MenuForm'),
    path(r'global', views.menu_global_view, name='MenuGlobal'),
    path(r'view/', views.menu_view, name='MenuView'),
    path(r'edit/<int:id>', views.menu_edit, name='MenuEdit'),
    path(r'edit/update/<int:id>', views.menu_update, name='MenuUpdate'),
    path(r'delete/<int:id>', views.menu_delete, name='MenuDelete'),
    path(r'order/<int:id>', views.order_edit, name='OrderFood'),
    # path(r'order/update/<int:id>', views.order_placed, name='MenuUpdate'),
    # path(r'edit/update/<int:id>', views.menu_update, name='MenuUpdate'),
    # path(r'order/update/<int:id>', views.order_placed, name='OrderUpdate'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)