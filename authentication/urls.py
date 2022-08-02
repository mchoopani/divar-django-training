from django.urls import path
from .views import signup_

urlpatterns = [
    path('signup/', signup_, name='signup'),
    path('login/', signup_, name='login'),  # TODO
]
