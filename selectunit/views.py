from django.contrib.auth.decorators import login_required, permission_required
from django.urls import reverse

from authentication.models import CustomUser as User
from django.shortcuts import render, redirect
from .permissions import is_admin
from authentication.forms import EditProfileForm
from selectunit.forms import UnitForm, ChanceForm
from selectunit.models import Unit


@login_required(login_url='login')
def profile(request):
    return render(request, 'selunit/profile.html', context={
        'chances': request.user.chance_set.all() if request.user.is_prof() else []
    })


@login_required(login_url='login')
def edit_profile(request):
    if request.method == 'GET':
        return render(request, 'selunit/edit_profile.html', context={
            'form': EditProfileForm()
        })
    else:
        form = EditProfileForm(data=request.POST, files=request.FILES, instance=User.objects.get(username=request.user.username))
        if form.is_valid():
            form.save()
            return redirect('profile')
        else:
            return render(request, 'selunit/edit_profile.html', context={
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


@login_required(login_url='login')
def all_units(request):
    return render(request, 'selunit/all_units.html', context={
        'units': Unit.objects.all()
    })


@login_required(login_url='login')
def chance(request):
    if request.method == 'GET':
        return render(request, 'selunit/chance.html', context={
            'form': ChanceForm()
        })
    if request.method == 'POST':
        form = ChanceForm(data=request.POST)
        if form.is_valid():
            chance_ = form.save()
            chance_.professor = request.user
            chance_.save()
            return redirect(reverse('index'))
        else:
            return render(request, 'selunit/chance.html', context={
                'form': form
            })
