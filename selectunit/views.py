from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .permissions import is_admin
from authentication.forms import EditProfileForm
from selectunit.forms import UnitForm
from selectunit.models import Unit


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


@is_admin
def unit_panel(request):
    if request.method == 'GET':
        return render(request, 'selunit/tasks.html', context={
            'form': UnitForm()
        })
    elif request.method == 'POST':
        form = UnitForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('panel')

        else:
            return render(request, 'selunit/tasks.html', context={
                'form': form
            })


def all_units(request):
    return render(request, 'selunit/all_units.html', context={
        'units': Unit.objects.all()
    })
