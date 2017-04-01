#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordResetForm, PasswordChangeForm
from django.contrib.auth import get_user_model
from django.contrib.auth import password_validation

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Field, HTML, Submit
from crispy_forms.bootstrap import PrependedText, FormActions, StrictButton

from book.helpers import *
from .models import *


class LoginForm(AuthenticationForm):
    """Form to allow user to log in to system"""
    username = forms.CharField(label="Username", max_length=30,
                               widget=forms.TextInput(
                                   attrs={'class': 'form-control',
                                          'name': 'username'}))
    password = forms.CharField(label="Password", max_length=30,
                               widget=forms.TextInput(
                                   attrs={'class': 'form-control',
                                          'name': 'password',
                                          'type': 'password'}))


class SignUpForm(UserCreationForm, PasswordResetForm):
    username = forms.CharField(
        label="Username",
        max_length=30,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'name': 'username'}))
    password1 = forms.CharField(
        label="Password",
        max_length=30, strip=False,
        widget=forms.PasswordInput(
            attrs={'class': 'form-control',
                   'name': 'password',
                   'type': 'password'}))
    password2 = forms.CharField(
        label="Password confirmation",
        strip=False,
        max_length=30,
        widget=forms.PasswordInput(
            attrs={'class': 'form-control',
                   'name': 'password confirmation',
                   'type': 'password'}))
    email = forms.CharField(
        label="email address",
        max_length=60,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'name': 'email address'}))

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ['username', 'email', 'password1', 'password2']


class ChangePassword(PasswordChangeForm):
    old_password = forms.CharField(label="Current Password", widget=forms.PasswordInput(attrs={'name': 'old_password'}),)
    password1 = forms.CharField(
        label="Password", max_length=30, strip=False,
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   'name': 'new password',
                   'type': 'password'}))
    password2 = forms.CharField(label="Password confirmation", strip=False, max_length=30,
                                widget=forms.TextInput(attrs={'class': 'form-control',
                                                              'name': 'new password confirmation',
                                                              'type': 'password'}))

    def __init__(self, *args, **kwargs):
        super(ChangePassword, self).__init__(*args, **kwargs)
        self.helper = password_change_helper
        # self.fields['password1'].label = ""

    class Meta:
        model = get_user_model()
        fields = ['old_password', 'password1', 'password2']


class AddBookForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AddBookForm, self).__init__(*args, **kwargs)
        self.helper = add_book_helper

    class Meta:
        model = Book
        fields = ['name', 'price', 'author', 'pub', 'published_date', 'image']


class EditBookForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EditBookForm, self).__init__(*args, **kwargs)
        self.helper = add_book_helper

    class Meta:
        model = Book
        fields = ['name', 'price', 'author', 'pub', 'published_date', 'image']


# class CustomModelFilter(forms.ModelChoiceField):
#
#     def label_from_instance(self, obj):
#         return "{}".format(obj.name)


class SearchBookForm(forms.Form):
    name = forms.CharField(max_length=100)
    author = forms.CharField(max_length=100)
    pub = forms.CharField(max_length=100)

    def __init__(self, *args, **kwargs):
        super(SearchBookForm, self).__init__(*args, **kwargs)
        self.helper = search_helper
        # self.fields["author"].widget = forms.widgets.TextInput()
        # # self.fields["author"].help_text = "Name of author"
        # # self.fields["author"].queryset = Book.objects.all()
        self.fields['name'].required = False
        self.fields['author'].required = False
        self.fields['pub'].required = False

    class Meta:
        model = Book
        fields = ['name', 'author', 'pub']
