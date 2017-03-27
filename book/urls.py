from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views
from django.contrib.auth.forms import *

from details.forms import LoginForm, SignUpForm
from details.views import index, register, change_password, activate_new_user

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^register/$', register, name='signup'),
    url(r'^activate/(?P<pk>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        activate_new_user, name='activate_user'),
    url(r'^login/$', views.login,
        {'template_name': 'l.html', 'authentication_form': LoginForm, },
        name='login'),
    url(r'^logout/$', views.logout, {'next_page': '/login'}),
    url(r'', include('details.urls')),
    url(r'^password_change', change_password, name="password_change")
    # url(r'^accounts/', include('registration.backends.simple.urls')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
