from django.db import models
from cuentas.models import Account

# Create your models here.

class Transaction(models.Model):
    TYPES = (
        ('Deposito', 'Deposito'),
        ('Retiro', 'Retiro'),
        ('Transferencia', 'Transferencia')
    )
    amount = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=20, choices=TYPES)
    idUser = models.ForeignKey(Account, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return str(self.amount)
