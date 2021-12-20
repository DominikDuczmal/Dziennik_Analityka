from django import forms
from django.forms import ModelForm
from .models import LABORATORY, Supervisor, Analyst
from django.contrib.auth.models import User

class AnalystSearchForm(forms.Form):
    last_name = forms.CharField(label='Nazwisko analityka')

class AnalystAddForm(forms.Form):
    analyst_lab = forms.ChoiceField(choices=LABORATORY, label='Laboratorium')
    first_name = forms.CharField(label='Imię')
    last_name = forms.CharField(label='Nazwisko')

