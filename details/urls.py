from django.conf.urls import url

from . import views
from .views import index,book,search_form 

urlpatterns = [
    url(r'^$', views.index, name='index'),
	url(r'^search-form/$', views.search_form, name='search'),
	url(r'^search/$', views.search, name='search'),
	# url(r'^error/$', views.error, name='error')
]