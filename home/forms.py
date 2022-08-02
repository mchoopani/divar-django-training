from django import forms


class CallWithMe(forms.Form):
    title = forms.CharField(label='عنوان', max_length=100, required=True)
    text = forms.CharField(widget=forms.Textarea(), label='متن', max_length=250, min_length=10, required=True)
    email = forms.EmailField(label='ایمیل', required=True)
