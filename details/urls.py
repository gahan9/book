from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views
from .forms import LoginForm

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # url(r'^search-form/$', views.search_form, name='search'),
    url(r'^search/$', views.search, name='search'),
    url(r'^product/(?P<book_id>[0-9]+)/$', views.product_page, name='product_page'),
    # url(r'^product/rated/$', views.user_rating, name='book_rated'),
]
