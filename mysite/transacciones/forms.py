from django import forms
from .models import *

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = '__all__'

class ResultForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = '__all__'
        exclude = ['timestamp']