from django.db import models
from login.models import User

# Create your models here.

class Contact(models.Model):
    idAcc = models.ForeignKey('Account', on_delete=models.CASCADE, blank=True, null=True, related_name='cuentas')

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    numAccount = models.IntegerField()
    saldo = models.FloatField(default=0)
    pin = models.CharField(max_length=4, default=0000)
    contact = models.ManyToManyField(Contact)
    
    def __str__(self):
        return str(self.numAccount)