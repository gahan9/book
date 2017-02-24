from django.conf.urls import url, include
from django.contrib import admin
#to use static files
from django.conf import settings
from django.conf.urls.static import static

#to import urls.py from details
from details import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('details.urls')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
