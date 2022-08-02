from django import forms
from django.contrib.auth.models import User


class SignupForm(forms.ModelForm):
    password1 = forms.CharField(label='رمز عبور', widget=forms.PasswordInput(), max_length=200)
    password2 = forms.CharField(label='تکرار رمز عبور', widget=forms.PasswordInput(), max_length=200)

    def clean(self):
        if self.cleaned_data['password1'] != self.cleaned_data['password2']:
            raise forms.ValidationError("passwords don't match!")
        return self.cleaned_data

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
