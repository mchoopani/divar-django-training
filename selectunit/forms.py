from django import forms
from .models import Unit


class CallWithMe(forms.Form):
    title = forms.CharField(label='عنوان', max_length=100, required=True)
    text = forms.CharField(label='متن', max_length=250, min_length=10, required=True)
    email = forms.EmailField(label='ایمیل', required=True)


class UnitForm(forms.ModelForm):
    class Meta:
        model = Unit
        fields = '__all__'
