from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
    path('stock/', views.stock, name='stock'),
    path('delivery/', views.delivery, name='delivery'),
    path('boxes/', views.boxes, name='boxes'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
