from django.db import models
from django.contrib.auth.models import AbstractUser
import utils

class CustomUser(AbstractUser):
    gender = models.CharField(choices=(
        ('F', 'Female'),
        ('M', 'Male')
    ), max_length=1)
    bio = models.TextField()
    photo = models.ImageField()

    def is_prof(self):
        return utils.is_professor(self)
