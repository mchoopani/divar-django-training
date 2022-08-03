from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from .models import CustomUser as User
from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import SignupForm


def signup_(request):
    if request.method == 'GET':
        return render(request, 'auth/signup.html', context={
            'form': SignupForm()
        })
    elif request.method == 'POST':
        form = SignupForm(data=request.POST)
        if form.is_valid():
            try:
                user = User(first_name=form.cleaned_data['first_name'],
                            last_name=form.cleaned_data['last_name'],
                            username=form.cleaned_data['username'],
                            email=form.cleaned_data['email'])
                user.set_password(form.cleaned_data['password1'])
                user.save()
                user.groups.add(Group.objects.get(name=('Professor' if form.cleaned_data['group'] == '0' else 'Student')))
            except Exception as e:
                return render(request, 'auth/signup.html', context={
                    'form': SignupForm(),
                    'error': True,
                    'error_message': str(e)
                })
            return redirect('login')
        else:
            return render(request, 'auth/signup.html', context={
                'form': SignupForm(),
                'error': True,
                'error_message': form.errors
            })


def login_(request):
    if request.method == 'GET':
        return render(request, 'auth/login.html', context={
            'error': request.GET.get('error', False),
            'error_message': request.GET.get('error_message')
        })
    elif request.method == 'POST':
        user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
        if user:
            login(request, user)
            return redirect(request.GET.get('next', '/'))
        else:
            if User.objects.filter(username=request.POST.get('username')).count() == 0:
                message = 'نام کاربری اشتباه است.'
            else:
                message = 'گذرواژه نادرست است'
            return redirect(reverse('login') + f'?error=true&error_message={message}')


def logout_(request):
    logout(request)
    return redirect('index')
