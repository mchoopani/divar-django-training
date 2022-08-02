from django.urls import path
from .views import signup_, login_, logout_

urlpatterns = [
    path('signup/', signup_, name='signup'),
    path('login/', login_, name='login'),
    path('logout/', logout_, name='logout'),  # TODO
]
