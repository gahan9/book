from django.conf.urls import url, include
from django.contrib.auth import views as auth_views

from . import views
from .forms import *

urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name='index'),
    url(r'^product/(?P<book_id>[0-9]+)/$', views.product_page, name='product_page'),
    url(r'^publisher/(?P<publisher_id>[0-9]+)/$', views.publisher_page, name='publisher_page'),
    url(r'^author/(?P<author_id>[0-9]+)/$', views.author_page, name='author_page'),
    url(r'^delete-entry/(?P<pk>\d+)/$', views.BookDeleteView.as_view(), name='delete_book'),
    url(r'^stock-availability', views.ToggleStockAvailability.as_view(), name='stock_change'),
    url(r'^book-create', views.BookCreate.as_view(), name='add_book'),
    url(r'^book-edit/(?P<pk>\d+)/$', views.BookEditView.as_view(), name='edit_book'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
