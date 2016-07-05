from django import forms
from .models import Patients
from django.contrib.auth.forms import AuthenticationForm
class PatientForm(forms.ModelForm):

    class Meta: #to tell django which model should be used to create this form (model = patient)
        model = Patients
        fields = ('firstname', 'lastname','location',
        'level','age','comment','gender')

class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    password = forms.CharField(label="Password", max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'password'}))
