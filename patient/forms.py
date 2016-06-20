from django import forms

# class PersonDetailsForm(forms.Form):
#     firstname = forms.CharField(max_length=100)
#     lastname = forms.CharField(max_length=100)
#     location = forms.TextField()
#     level = forms.IntegerField()
#     age = forms.IntegerField()
#     comment = forms.TextField()

#     age = forms.IntegerField()

from .models import Patients

class PatientForm(forms.ModelForm):

    class Meta: #to tell django which model should be used to create this form (model = patient)
        model = Patients
        fields = ('firstname', 'lastname','location',
        'level','age','comment','gender')