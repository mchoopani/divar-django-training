from django.shortcuts import redirect
from django.urls import reverse


def is_admin(func):
    def wrap(request, *args, **kwargs):
        if not request.user.is_superuser:
            return redirect(reverse('all_units'))
        return func(request, *args, **kwargs)
    return wrap