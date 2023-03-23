from django.shortcuts import render, redirect
from django.views import View, generic
from .forms import TransactionForm
from .models import Transaction
from cuentas.models import Account
from django.contrib import messages

# Create your views here.

class TransactionList(generic.ListView):
    model = Transaction

class Home(View):
    def get(self, request):
        form = TransactionForm()
        context = {'form': form}
        return render(request, 'transacciones/transacciones.html', context)

    def post(self, request):
        form = TransactionForm(request.POST)
        if form.is_valid():
            llenado = form.save(commit=False)
            cuentas = Account.objects.all()
            num = str(llenado.idUser)
            if llenado.type == 'Deposito':
                for c in cuentas:
                    if c.numAccount == int(num):
                        c.saldo = c.saldo + llenado.amount
                        c.save()
            elif llenado.type == "Retiro":
                for c in cuentas:
                    if c.numAccount == int(num):
                        if c.saldo < llenado.amount:
                            messages.warning(request, 'El saldo es insuficiente, vuelve a intentarlo')
                            return redirect('transacciones')
                        else:
                            c.saldo = c.saldo - llenado.amount
                            c.save()
            llenado.save()
            messages.success(request, 'Transaccion realizada')
            return redirect('transacciones')
        