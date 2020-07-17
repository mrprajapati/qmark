from django.shortcuts import render, redirect, HttpResponse
from django.views.generic.edit import FormView
from accounts.forms import RegistrationForm, LoginForm
from django.contrib.auth import login, authenticate
from bootstrap_modal_forms.generic import BSModalLoginView
from django.urls import reverse_lazy
from django.contrib.auth.views import LogoutView


class RegisterView(FormView):
    form_class = RegistrationForm
    template_name = 'register.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.save()
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password1')
        account = authenticate(email=email, password=password)
        login(self.request, account)
        return super().form_valid(form)


class LoginView(BSModalLoginView):
    form = LoginForm
    template_name = 'login.html'
    success_message = 'You are logged in.'
    success_url = reverse_lazy('index')


class LogoutView(LogoutView):
    success_message = 'You are logged out.'
