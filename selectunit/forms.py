from django import forms
from .models import Unit, Chance


class CallWithMe(forms.Form):
    title = forms.CharField(label='عنوان', max_length=100, required=True)
    text = forms.CharField(label='متن', max_length=250, min_length=10, required=True)
    email = forms.EmailField(label='ایمیل', required=True)


class UnitForm(forms.ModelForm):
    start_time = forms.TimeField(label='ساعت شروع', input_formats=['%H:%M'])
    end_time = forms.TimeField(label='ساعت پایان', input_formats=['%H:%M'])

    class Meta:
        model = Unit
        fields = '__all__'
        labels = {
            "name": "نام واحد",
            "college": "نام دانشکده",
            "end_time": "ساعت پایان",
            "first_day": "روز اول",
            "start_time": "ساعت شروع",
            "professor_name": "نام استاد",
            "second_day": "روز دوم",
            "group_number": "شماره گروه",
        }


class ChanceForm(forms.ModelForm):
    def clean(self):
        start = self.cleaned_data['start_time']
        end = self.cleaned_data['end_time']
        if start > end:
            raise forms.ValidationError('زمان شروع نباید از پایان بزرگ تر باشد')

        for chance in Chance.objects.all():
            if start <= chance.start_time < end or start < chance.end_time <= end:
                raise forms.ValidationError('این بازه زمانی با دیگر فرصت های شما تداخل دارد.')
        return self.cleaned_data

    class Meta:
        model = Chance
        fields = '__all__'
        exclude = ('professor',)
        labels = {
            'capacity': 'ظرفیت',
            'start_time': 'زمان شروع',
            'end_time': 'زمان پایان'
        }
