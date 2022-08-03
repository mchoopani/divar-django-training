from django.db import models
from django.contrib.auth.models import AbstractUser, Group

class CustomUser(AbstractUser):
    gender = models.CharField(choices=(
        ('F', 'Female'),
        ('M', 'Male')
    ), max_length=1)
    bio = models.TextField()
    photo = models.ImageField()

    def is_prof(self):
        prof_group = Group.objects.get(name='Professor')

        if prof_group in self.groups.all():
            return True
        return False
