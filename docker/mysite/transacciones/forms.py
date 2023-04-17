from django import forms
from .models import Transaction
from cuentas.models import Account

class TransactionForm(forms.ModelForm):
    pin = forms.CharField(max_length=4)

    class Meta:
        model = Transaction
        fields = '__all__'