from django import forms
from .models import Patient, Interview

class PatientForm(forms.ModelForm):

    name = forms.CharField(min_length=1, max_length=10)
    age = forms.IntegerField(min_value=5, max_value=150)
    weight = forms.FloatField(min_value=3.0, max_value=300.0)
    height = forms.FloatField(min_value=20.0, max_value=300.0)
    mbti = forms.CharField(min_length=4, max_length=4)

    class Meta:
        model = Patient
        # fields = '__all__'
        fields = ('name', 'age', 'weight', 'height', 'mbti')


class InterviewForm(forms.ModelForm):

    date = forms.DateField(widget=forms.DateInput(format='%Y-%m-%d', attrs={ 'type': 'date', }))

    class Meta:
        model = Interview
        fields = ('content', 'date',)