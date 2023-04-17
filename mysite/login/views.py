from django.shortcuts import render, redirect
from .forms import UserForm
from django.views import View
from .models import User
from django.contrib import messages

# Create your views here.

class UserAdd(View):
    def get(self, request):
        form = UserForm()
        context = {'form': form}
        return render(request, 'login/add_user.html', context)
    
    def post(self, request):
        form = UserForm(request.POST)
        if form.is_valid():
            llenado = form.save(commit=False)
            users = User.objects.filter()
            llenado.save()
            messages.success(request, 'Usuario registrado')
            return redirect('adduser')