from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Contact(models.Model):
    idAcc = models.ForeignKey('Account', on_delete=models.CASCADE, blank=True, null=True, related_name='cuentas')

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    numAccount = models.IntegerField()
    saldo = models.IntegerField()
    pin = models.CharField(max_length=4)
    contact = models.ManyToManyField(Contact)
    
    def __str__(self):
        return str(self.numAccount)

class Transaction(models.Model):
    TYPES = (
        ('Deposito', 'Deposito'),
        ('Retiro', 'Retiro'),
        ('Transferencia', 'Transferencia')
    )
    amount = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=20, choices=TYPES)
    idUser = models.ForeignKey('Account', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return str(self.amount)
