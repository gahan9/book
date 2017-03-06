from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views
from django.views.generic import RedirectView

from django_otp.forms import OTPAuthenticationForm
from django_otp.views import login
from details.forms import LoginForm, SignUpForm
from details.views import register, change_password

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^login/$', views.login, {'template_name': 'l.html', 'authentication_form': OTPAuthenticationForm, }, name='login'),
    # url(r'^register/$', register, {'template_name': 'register.html', 'create_user': SignUpForm,},name='signup'),
    url(r'^register/$', register, name='signup'),
    # url(r'^/$', registration_complete, name = 'registration completed'),
    url(r'^login/$', views.login, {'template_name': 'l.html', 'authentication_form': LoginForm, }, name='login'),
    url(r'^logout/$', views.logout, {'next_page': '/login'}),
    url(r'', include('details.urls')),
    url(r'^password_change', change_password, name="password change")
    # url(r'^register/complete/$', RedirectView.as_view(url='/login/'), name='my_custom_complete'),
    # url(r'^accounts/', include('registration.backends.simple.urls')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
