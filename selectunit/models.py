from django.db import models

class Unit(models.Model):
    college = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    group_number = models.IntegerField()
    professor_name = models.CharField(max_length=100)
    start_time = models.TimeField()
    end_time = models.TimeField()
    first_day = models.CharField(choices=(
        ('1', 'شنبه'),
        ('2', 'یکشنبه'),
        ('3', 'دوشنبه'),
        ('4', 'سه‌شنبه'),
        ('5', 'چهارشنبه'),
        ('6', 'پنج‌شنبه'),
        ('7', 'جمعه'),
    ), max_length=1)
    second_day = models.CharField(choices=(
        ('1', 'شنبه'),
        ('2', 'یکشنبه'),
        ('3', 'دوشنبه'),
        ('4', 'سه‌شنبه'),
        ('5', 'چهارشنبه'),
        ('6', 'پنج‌شنبه'),
        ('7', 'جمعه'),
    ), max_length=1)
