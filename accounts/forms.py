from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from accounts.models import Account


class RegistrationForm(UserCreationForm):

    email = forms.EmailField(
        max_length=60, help_text='Email Require')

    class Meta:
        model = Account
        # widgets = {
        #     'name': forms.TextInput(attrs={'placeholder': 'Name', 'autofocus': False}),
        #     'email': forms.EmailInput(attrs={'placeholder': 'Email', 'autofocus': False}),
        #     'password1': forms.PasswordInput(attrs={'placeholder': 'Password'}),
        #     'Password2': forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}),

        # }
        fields = ("email", "name", "password1", "password2")
        # fields = '__all__'


class LoginForm(AuthenticationForm):
    class Meta:
        model = Account
        fields = ['email', 'password']
