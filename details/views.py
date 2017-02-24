from django.shortcuts import render, render_to_response
from django.http import HttpResponse, Http404
from django.contrib.auth.models import User
from django.template import loader, RequestContext
from django.db.models import Q, Prefetch
from .models import Author,Publisher,book

def index(request):
	"""	Show all data from database """
	bl = book.objects.all().order_by('name')
	return render(request,'book.html',{'bl': bl})

def search_form(request):
	"""	Show data from result of Query"""
	return render('result.html')

def search(request):
	""" Implemented to sniff database """
	ls = {"pk": request.GET.get('id', None),
		   "name__icontains": request.GET.get('name', None),
		   "author__name__icontains": request.GET.get('author', None), 
		   "pub__name__icontains": request.GET.get('publication', None)
		 }

	req_data = dict(filter(lambda x:x[1] , ls.items()))

	id_ = request.GET.get('id', None)
	if req_data:
		books = book.objects.filter(**req_data)
		return render(request, 'results.html', {'books' : books}, {'query' : id_})

	# elif 'name' in request.GET and request.GET['name']:
	# 	books = book.objects.filter(name__icontains = request.GET['name'])
	# 	return render(request, 'results.html', {'books' : books}, {'query' : request.GET['name']})

	# elif 'author' in request.GET and request.GET['author']:
	# 	books = book.objects.filter(author__name__icontains = request.GET['author'])

	# 	return render(request, 'results.html', {'books' : books}, {'query' : request.GET['author']})

	# elif 'publication' in request.GET and request.GET['publication']:
	# 	books = book.objects.filter(pub__name__icontains = request.GET['publication'])
	# 	return render(request, 'results.html', {'books' : books}, {'query' : request.GET['publication']})
	
	else:
		return render(request, 'error.html')