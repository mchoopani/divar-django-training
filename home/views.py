from django.shortcuts import render

from home.forms import CallWithMe


def index(request):
    return render(request, 'home/index.html')


def call_with_us(request):
    if request.method == 'GET':
        return render(request, 'home/callwithus.html', context={'form': CallWithMe()})
    elif request.method == 'POST':
        form = CallWithMe(data=request.POST)
        if form.is_valid():
            return render(request, 'home/callwithus.html', context={
                'success': True
            })
        else:
            return render(request, 'home/callwithus.html', context={
                'success': False,
                'error': True,
                'error_message': form.errors
            })
