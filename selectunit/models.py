from django.db import models

class Unit(models.Model):
    college = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    group_number = models.IntegerField()
    professor_name = models.CharField(max_length=100)
    start_time = models.TimeField()
    end_time = models.TimeField()
    first_day = models.CharField(choices=(
        ('شنبه', 'شنبه'),
        ('یک‌شنبه', 'یکشنبه'),
        ('دوشنبه', 'دوشنبه'),
        ('سه‌شنبه', 'سه‌شنبه'),
        ('چهار‌شنبه', 'چهارشنبه'),
    ), max_length=50)
    second_day = models.CharField(null=True, blank=True, choices=(
        ('شنبه', 'شنبه'),
        ('یک‌شنبه', 'یکشنبه'),
        ('دوشنبه', 'دوشنبه'),
        ('سه‌شنبه', 'سه‌شنبه'),
        ('چهار‌شنبه', 'چهارشنبه'),
    ), max_length=50)
