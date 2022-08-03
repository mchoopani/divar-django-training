from django.contrib.auth.models import Group


def is_professor(user):
    prof_group = Group.objects.get(name='Professor')
    if prof_group in user.groups.all():
        return True
    return False
