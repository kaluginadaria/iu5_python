from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse, HttpResponseNotFound
from django import forms
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, View
from django.views.generic import DetailView
import datetime

from hwApp.paginator import paginate
from .models import *


def groups_view(request):

    d = {group.id: Comment.objects.filter(group=group).count()  for group in Group.objects.all()}
    print(d)
    group1 = Group.objects.all()
    page = request.GET.get('page')
    tag = Genre.objects.all()


    return render(request, "home.html", {'group_list': d, 'tag': tag, 'paginator': paginate(group1, page)})


class CommentForm(forms.Form):
    text = forms.CharField(max_length=100, widget=forms.Textarea(attrs={'class': 'form-control'}))


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


class GroupForm(forms.ModelForm):
    class Meta(object):
        model = Group
        fields = ['name', 'genre', 'description', 'pic']

    def save(self):
        group = Group()

        group.name = self.cleaned_data.get('name')

        group.genre = self.cleaned_data.get('genre')

        group.description = self.cleaned_data.get('description')
        group.pic = self.cleaned_data.get('pic')
        group.save()


def add(request):
    if request.method == 'POST':
        name1 = request.POST.get('name')
        user = Person.objects.get(user=request.user)
        member = request.POST.get('member')
        date = request.POST.get('date')
        genres = request.POST.get('genre').split(' ')
        description = request.POST.get('description')
        pic1 = request.FILES.get('pic')
        rate = 0
        group1 = Group(user=user, name=name1, description=description, rating=rate,
                       pic=pic1)
        group1.save()
        print(group1.id)
        for i in genres:
            try:
                genre = Genre.objects.get(name=i)
                group1.genre.add(genre)

            except:
                genre = Genre(name=i)
                genre.save()
                group1.genre.add(genre)
            group1.save()
        group1.save()

        return HttpResponseRedirect('/item-' + str(group1.id))

    return render(request, 'add.html', locals())


# регистрация
def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        avatar = request.FILES.get('avatar')
        is_val = form.is_valid()
        data = form.cleaned_data

        print(avatar)

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
            pers.avatar = avatar
            pers.save()
            return HttpResponseRedirect('/authorization')
    else:
        form = RegistrationForm()
    tags = Genre.objects.all()
    return render(request, 'registration.html', {'form': form, 'tag': tags})


# авторизация django
def authorization(request):
    if request.method == 'POST':
        form = AuthorizationForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
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
    tags = Genre.objects.all()
    return render(request, 'authorization.html', {'form': form, 'tag': tags})


# успешная авторизация django
@login_required(login_url='/authorization')
def success_authorization(request):
    return HttpResponseRedirect('/')


# выход
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')


def OneGroup(request, pk):
    try:
        group = Group.objects.get(id=pk)
    except:
        return HttpResponseNotFound('<h1>No Page Here</h1>')
    page = request.GET.get('page')
    comment = Comment.objects.filter(group=group)
    tag = Genre.objects.all()
    if request.method == 'POST':

        if request.user.is_authenticated:

            form = CommentForm(request.POST)
            is_val = form.is_valid()
            data = form.cleaned_data
            t = data['text']

            if is_val:
                comment = Comment.objects.create(
                    user=request.user.person,
                    group=group,
                    text=data['text'],
                )
                comment.save()

                return HttpResponseRedirect('/item-' + str(group.id))
        else:
            return HttpResponseRedirect('/authorization/')

    else:
        form = CommentForm()
    return render(request, 'object.html',
                  {'group': group, 'paginator': paginate(comment, page), 'form': form, 'tag': tag})
