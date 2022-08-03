from django.shortcuts import render
from django.core.mail import send_mail
import vahed_project.settings as setting
from home.forms import CallWithMe


def index(request):
    return render(request, 'home/index.html')


def call_with_us(request):
    if request.method == 'GET':
        return render(request, 'home/callwithus.html', context={'form': CallWithMe()})
    elif request.method == 'POST':
        form = CallWithMe(data=request.POST)
        if form.is_valid():
            try:
                send_mail(
                    subject=form.cleaned_data['title'],
                    message=f'{form.cleaned_data["email"]} says: \n{form.cleaned_data["text"]}',
                    from_email=setting.EMAIL_HOST_USER,
                    recipient_list=setting.ADMINS_EMAILS,
                    fail_silently=False,
                )
            except Exception as _:
                return render(request, 'home/callwithus.html', context={
                    'success': False,
                    'error': True,
                    'error_message': 'مشکلی در ارسال ایمیل وجود دارد.'
                })
            return render(request, 'home/callwithus.html', context={
                'success': True
            })
        else:
            return render(request, 'home/callwithus.html', context={
                'success': False,
                'error': True,
                'error_message': form.errors
            })
