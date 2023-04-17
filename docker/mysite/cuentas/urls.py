from django.urls import path, include
from . import views
from .views import AddAccount

urlpatterns = [
    path('add_account', AddAccount.as_view(), name='add_account'),
]