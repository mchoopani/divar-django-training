from django.shortcuts import render
from .forms import SignupForm


def signup_(request):
    if request.method == 'GET':
        return render(request, 'auth/signup.html', context={
            'form': SignupForm()
        })
