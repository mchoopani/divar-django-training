from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from authentication.forms import EditProfileForm


@login_required(login_url='login')
def profile(request):
    return render(request, 'selunit/profile.html')


@login_required(login_url='login')
def edit_profile(request):
    if request.method == 'GET':
        return render(request, 'selunit/edit_profile.html', context={
            'form': EditProfileForm()
        })
    else:
        form = EditProfileForm(data=request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            if first_name == '':
                first_name = request.user.first_name
            last_name = form.cleaned_data['last_name']
            if last_name == '':
                last_name = request.user.last_name
            User.objects.filter(username=request.user.username).update(first_name=first_name, last_name=last_name)
            return redirect('profile')
        else:
            render(request, 'selunit/edit_profile.html', context={
                'form': form
            })
