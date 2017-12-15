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

class OrdersView(ListView):
    model = Orders
    template_name = 'home.html'
    context_object_name = 'orders_list'

def registration_form(request):
    errors = {}
    request.encoding = 'utf-8'
    if request.method == 'POST':
        username = request.POST.get('username')
        if not username:
            errors['uname'] = 'Введите логин'
        elif len(username) < 5:
            errors['uname'] = 'Длина логина должна быть не меньше 5 символов'

        if User.objects.filter(username=username).exists():
            errors['uname'] = 'Такой логин уже занят'

        password = request.POST.get('password')
        if not password:
            errors['psw'] = 'Введите пароль'
        elif len(password) < 8:
            errors['psw'] = 'Длина пароля должна быть не меньше 8 символов'

        password2 = request.POST.get('password2')
        if password != password2:
            errors['psw2'] = 'Пароли должны совпадать'

        email = request.POST.get('email')
        if not email:
            errors['email'] = 'Введите email'

        last_name = request.POST.get('last_name')
        if not last_name:
            errors['lname'] = 'Введите фамилию'

        first_name = request.POST.get('first_name')
        if not first_name:
            errors['fname'] = 'Введите имя'

        if not errors:

            user = User.objects.create_user(username, email, password)
            cust = Customer()
            cust.user = user
            # cust.customer_name = username
            # cust.email = email
            cust.last_name = last_name
            cust.first_name = first_name

            cust.save()
            return HttpResponseRedirect('/authorization_form')
        else:
            context = {'errors': errors, 'username': username, 'email': email, 'last_name': last_name,
                       'first_name': first_name}
            return render(request, 'registration_form.html', context)

    return render(request, 'registration_form.html', {'errors': errors})


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
            cust = Customer()
            cust.user = user
            cust.first_name = data['first_name']
            cust.last_name = data['last_name']

            cust.save()
            return HttpResponseRedirect('/authorization')
    else:
        form = RegistrationForm()

    return render(request, 'registration.html', {'form': form})


# авторизация вручную
def authorization_form(request):
    errors = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        if not username:
            errors['uname'] = 'Введите логин'

        password = request.POST.get('password')
        if not password:
            errors['psw'] = 'Введите пароль'

        user = authenticate(request, username=username, password=password)
        if user is None and 'uname' not in errors.keys() and 'psw' not in errors.keys():
            errors['login'] = 'Логин или пароль введены неверно'

        if not errors:
            login(request, user)
            return HttpResponseRedirect('/success_authorization_form')
        else:
            context = {'errors': errors}
            return render(request, 'authorization_form.html', context)

    return render(request, 'authorization_form.html', {'errors': errors})


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


# успешная авторизация вручную
def success_authorization_form(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/authorization')


# успешная авторизация django
@login_required(login_url='/authorization')
def success_authorization(request):
    return HttpResponseRedirect('/')


# выход
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')
