from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls), # при переходе на админ будет открываться панель админа
    path('', include('handmade_catalog_web.urls')),
    path('news/', include('news.urls')),
    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
