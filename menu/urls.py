from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path(r'', views.Menu_form, name='MenuForm'),
    path(r'global', views.menu_global_view, name='MenuGlobal'),
    path(r'delete/<int:id>', views.menu_delete, name='MenuDelete'),
    path(r'view/', views.menu_view, name='MenuView'),
    path(r'edit/<int:id>', views.menu_edit, name='MenuEdit'),
    path(r'edit/update/<int:id>', views.menu_update, name='MenuUpdate'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)