from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
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
            'error_message': 'نام کاربری یا رمز عبور اشتباه وارد شده است.'
        })
    elif request.method == 'POST':
        user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
        if user:
            login(request, user)
            return redirect(request.GET.get('next', '/'))
        else:
            return redirect(reverse('login') + '?error=true')


def logout_(request):
    logout(request)
    return redirect('index')
