from django.contrib import admin
from django.urls import path, include
from WebShop.views import index, contact
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name='index'),
    path('', contact, name='contact'),
    path('admin/', admin.site.urls),
    path('items/', include('item.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
