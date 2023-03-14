from django import forms
from .models import Account, Contact

class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = '__all__'