from django.shortcuts import render, redirect
from .models import Account
from .forms import AccountForm
from django.views import View
from django.contrib import messages

# Create your views here.

class AddAccount(View):
    def get(self, request):
        form = AccountForm()
        context = {'form': form}
        return render(request, 'cuentas/add_account.html', context)

    def post(self, request):
        form = AccountForm(request.POST)
        if form.is_valid():
            llenado = form.save(commit=False)
            transactions = Account.objects.filter()
            llenado.save()
            messages.success(request, 'Cuenta agregada')
            return redirect('add_account')