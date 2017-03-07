from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse, Http404, request
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.contrib.auth.tokens import PasswordResetTokenGenerator as activation_user
from django.template import loader
from django.urls import reverse

from .forms import SignUpForm, ChangePassword
from .models import Author, Publisher, book


def register(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            # form.save()
            new_user_name = form.cleaned_data['username']
            new_user_password = form.cleaned_data['password1']
            new_user_email = form.cleaned_data['email']
            new_user = User.objects.create_user(username=new_user_name,
                                                email=new_user_email,
                                                password=new_user_password)
            new_user.is_active = False
            new_user.save()
            new_user_token = activation_user().make_token(new_user)
            # url = reverse('activate_user',
            # kwargs={'pk':new_user.id, 'token':new_user_token})
            host = request.get_host()
            # var_url = 'http://'+ host + url
            # var_url = host + url

            # context = {'user': new_user, 'token': new_user_token}
            # email_message = EmailMultiAlternatives("Activate yourself",
            #  loader.render_to_string('error.html', context),
            # 'gahan@quixom.com', ['gahan@quixom.com'])
            # email_message.send()
            send_mail("Activate YOur Account",
                      loader.render_to_string('user_activate.html',
                                              {'pk':new_user.id,
                                               'token':new_user_token,
                                               'domain':host,
                                               'user': new_user_name}),
                      'gahan@quixom.com',
                      ['gahan@quixom.com'])
            # print(dir(new_user), new_user.natural_key(), sep='\n')
            return HttpResponseRedirect('/login/')
            # else:
            #     x = [v[0] for k, v in form.errors.items()]
            #     return HttpResponse(x)
    else:
        form = SignUpForm()
    return render(request, 'registration.html', {'form': form})

# def registration_complete(request):
#     return render_to_response('book.html')


def activate_new_user(request, pk, token):
    usr = User.objects.get(pk=pk)
    verified = activation_user().check_token(usr, token)
    if verified:
        usr.is_active = True
        usr.save()
        return HttpResponseRedirect('/')
    else:
        return HttpResponse("Invalid Verification Link")

def change_password(request):
    if request.method == 'POST':
        current_user = request.user.username
        reset_form = ChangePassword(request.POST,user=request.user)
        if reset_form.is_valid():
            u = User.objects.get(username__exact=current_user)
            u.set_password(reset_form.cleaned_data['password2'])
            u.save()
            return HttpResponseRedirect('/')
    else:
        reset_form = ChangePassword(user=request.user)
    return render(request, 'change_password.html', {'reset_form': reset_form})


def product_page(request, book_id):
    product = book.objects.filter(pk=book_id)
    if product != {}:
        return render(request, 'book_page.html', {'product': product})
    else:
        error = 'You have encountered incorrect product page'
        return render(request, 'error.html', {'error': error})


@login_required(login_url='login/')
def index(request):
    """	Show all data from database """
    bl = book.objects.all().order_by('-id')
    return render(request, 'book.html', {'bl': bl})


def search_form(request):
    """	Show data from result of Query"""
    return render('result.html')


def search(request):
    """ Implemented to sniff entries in database """
    ls = {"pk": request.GET.get('id', None),
          "name__icontains": request.GET.get('name', None),
          "author__name__icontains": request.GET.get('author', None),
          "pub__name__icontains": request.GET.get('publication', None)
          }

    req_data = dict(filter(lambda x: x[1], ls.items()))

    id_ = request.GET.get('id', None)

    if req_data:
        books = book.objects.filter(**req_data)
        return render(request, 'results.html', {'books': books},
                      {'query': id_})
    else:
        error = 'No match found'
        return render(request, 'error.html', {'error': error})
