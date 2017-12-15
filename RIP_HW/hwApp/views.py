from django.shortcuts import render
from django.http import HttpResponseRedirect
from django import forms
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView

from .models import *


# Create your views here.
def home(request):
    parameters = {
        'header': "Содержимое"
    }
    return render(request, 'home.html', context=parameters)


class GroupsView(ListView):
    model = Group
    template_name = 'home.html'
    context_object_name = 'group_list'


class PersonsView(ListView):
    model = Person
    template_name = 'home.html'
    context_object_name = 'persons_list'


# форма регистрации
class RegistrationForm(forms.Form):
    username = forms.CharField(min_length=5, label='Логин')
    password = forms.CharField(min_length=8, widget=forms.PasswordInput, label='Пароль')
    password2 = forms.CharField(min_length=8, widget=forms.PasswordInput, label='Повторите ввод')
    email = forms.EmailField(label='Email')
    last_name = forms.CharField(label='Фамилия')
    first_name = forms.CharField(label='Имя')


class AuthorizationForm(forms.Form):
    username = forms.CharField(label='Логин')
    password = forms.CharField(widget=forms.PasswordInput, label='Пароль')


# регистрация
def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        is_val = form.is_valid()
        data = form.cleaned_data
        if data['password'] != data['password2']:
            is_val = False
            form.add_error('password2', ['Пароли должны совпадать'])
        if User.objects.filter(username=data['username']).exists():
            form.add_error('username', ['Такой логин уже существует'])
            is_val = False

        if is_val:
            data = form.cleaned_data
            user = User.objects.create_user(data['username'], data['email'], data['password'])
            pers = Person()
            pers.user = user
            pers.first_name = data['first_name']
            pers.last_name = data['last_name']

            pers.save()
            return HttpResponseRedirect('/authorization')
    else:
        form = RegistrationForm()

    return render(request, 'registration.html', {'form': form})


# авторизация django
def authorization(request):
    if request.method == 'POST':
        form = AuthorizationForm(request.POST)
        print(form)
        data = form.cleaned_data

        if form.is_valid():
            user = authenticate(request, username=data['username'], password=data['password'])
            # user = authenticate(request, username='petrov',password='12345678')
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/success_authorization')
            else:
                form.add_error('username', ['Неверный логин или пароль'])
                # raise forms.ValidationError('Имя пользователя и пароль не подходят')

    else:
        form = AuthorizationForm()

    return render(request, 'authorization.html', {'form': form})


# успешная авторизация django
@login_required(login_url='/authorization')
def success_authorization(request):
    return HttpResponseRedirect('/')


# выход
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')
