from django import forms
from django.contrib.auth.models import User

from authentication.models import CustomUser


class SignupForm(forms.ModelForm):
    password1 = forms.CharField(label='رمز عبور', widget=forms.PasswordInput(), max_length=200)
    password2 = forms.CharField(label='تکرار رمز عبور', widget=forms.PasswordInput(), max_length=200)
    group = forms.ChoiceField(label='سمت', choices=(
        (0, 'استاد'),
        (1, 'دانشجو'),
    ))

    def clean(self):
        if self.cleaned_data['password1'] != self.cleaned_data['password2']:
            raise forms.ValidationError("passwords don't match!")
        return self.cleaned_data

    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email')


class EditProfileForm(forms.ModelForm):
    first_name = forms.CharField(label='نام', max_length=50, required=False)
    last_name = forms.CharField(label='نام خانوادگی', max_length=50, required=False)

    def clean_first_name(self):
        return self.instance.first_name if len(self.cleaned_data['first_name']) == 0 else self.cleaned_data[
            'first_name']

    def clean_last_name(self):
        return self.instance.last_name if len(self.cleaned_data['last_name']) == 0 else self.cleaned_data[
            'last_name']

    class Meta:
        model = CustomUser
        fields = (
            'first_name',
            'last_name',
            'bio',
            'gender',
            'photo'
        )
        labels = {
            'bio': 'زندگینامه',
            'gender': 'جنسیت'
        }
