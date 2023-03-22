from django import forms
from .models import Account, Contact

class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['user', 'numAccount', 'pin']