from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views
from .forms import LoginForm

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^search/$', views.search, name='search'),
    url(r'^product/(?P<book_id>[0-9]+)/$', views.product_page, name='product_page'),
    url(r'^publisher/(?P<publisher_id>[0-9]+)/$', views.publisher_page, name='publisher_page'),
    url(r'^author/(?P<author_id>[0-9]+)/$', views.author_page, name='author_page'),
    url(r'^delete_entry/', views.delete_entry),
    url(r'^stock_availability', views.stock_availability, name='stock_change')
]
