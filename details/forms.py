from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordResetForm
from django.contrib.auth import get_user_model
from django.contrib.auth import password_validation


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


class ChangePassword(forms.Form):
    old_password = forms.CharField(
        label="Old password",
        strip=False,
        widget=forms.PasswordInput(
            attrs={'name': 'old_password'}),
    )
    password1 = forms.CharField(
        label="Password",
        max_length=30, strip=False,
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   'name': 'new password',
                   'type': 'password'}))
    password2 = forms.CharField(
        label="Password confirmation",
        strip=False,
        max_length=30,
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   'name': 'new password confirmation',
                   'type': 'password'}))

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(ChangePassword, self).__init__(*args, **kwargs)

    def clean_password2(self):
        print("data")
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("The two password fields didn't match.")
        # self.username = self.cleaned_data.get('username')
        password_validation.validate_password(self.cleaned_data.get('password2'))
        return password2

    def clean_old_password(self):
        """
        Validates that the old_password field is correct.
        """
        print("sell")
        old_password = self.cleaned_data["old_password"]
        if not self.user.check_password(old_password):
            raise forms.ValidationError('Incorrect old password')
        return old_password

    class Meta:
        model = get_user_model()
        fields = ['old_password', 'password1', 'password2']
