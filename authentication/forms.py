from django import forms
from django.contrib.auth.models import User


class SignupForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput(), max_length=200)
    password2 = forms.CharField(widget=forms.PasswordInput(), max_length=200)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
