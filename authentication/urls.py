from django.urls import path
from .views import signup_, login_

urlpatterns = [
    path('signup/', signup_, name='signup'),
    path('login/', login_, name='login'),
    path('logout/', login_, name='logout'),  # TODO
]
