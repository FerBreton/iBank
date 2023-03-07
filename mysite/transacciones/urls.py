from django.urls import path, include
from . import views
from .views import *

urlpatterns = [
    path('', Home.as_view(), name='transacciones'),
]