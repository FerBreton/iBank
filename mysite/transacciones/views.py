from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from .forms import *
from .models import *
from django.contrib import messages
import datetime

# Create your views here.

class Home(View):
    def get(self, request):
        form = TransactionForm()
        transacciones = Transaction.objects.all()
        context = {'form': form, 'transacciones': transacciones}
        return render(request, 'index.html', context)

    def post(self, request):
        form = TransactionForm(request.POST)
        if form.is_valid():
            llenado = form.save(commit=False)
            transactions = Transaction.objects.filter(amount = llenado.amount, timestamp__gte = datetime.date.today(), type = llenado.type)
            llenado.save()
            messages.success(request, 'Transaccion realizada')
            return redirect('transacciones')
        