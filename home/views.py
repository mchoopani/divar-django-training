from django.shortcuts import render
from django.core.mail import send_mail

from home.forms import CallWithMe


def index(request):
    return render(request, 'home/index.html')


def call_with_us(request):
    if request.method == 'GET':
        return render(request, 'home/callwithus.html', context={'form': CallWithMe()})
    elif request.method == 'POST':
        form = CallWithMe(data=request.POST)
        if form.is_valid():

            send_mail(
                form.cleaned_data['title'],
                form.cleaned_data['text'],
                'choopani.m81@gmail.com',
                ['choopani.m81@gmail.com'],
                fail_silently=False,
            )
            return render(request, 'home/callwithus.html', context={
                'success': True
            })
        else:
            return render(request, 'home/callwithus.html', context={
                'success': False,
                'error': True,
                'error_message': form.errors
            })
