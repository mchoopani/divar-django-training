from django.urls import path

from .views import profile, edit_profile, unit_panel, all_units, chance

urlpatterns = [
    path('profile/', profile, name='profile'),
    path('profile/edit', edit_profile, name='edit_profile'),
    path('dashboard/', unit_panel, name='panel'),
    path('units/', all_units, name='all_units'),
    # path('search/'),
    path('chance', chance, name='chance')
]
