from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as a_views
from django.contrib.auth.forms import *
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

from details.forms import *
from details import views


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'authors', views.AuthorViewSet)
router.register(r'books', views.BookViewSet)
router.register(r'publishers', views.PublisherViewSet)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^register/$', views.register, name='signup'),
    url(r'^activate/(?P<pk>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate_new_user, name='activate_user'),
    url(r'^login/$', a_views.login,
        {'template_name': 'l.html', 'authentication_form': LoginForm, },
        name='login'),
    url(r'^logout/$', a_views.logout, {'next_page': '/login'}),
    url(r'', include('details.urls')),
    url(r'^password_change', views.ChangeProfilePassword.as_view(), name="password_change"),
    # url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
