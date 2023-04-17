from django.urls import path, include
from . import views
from .views import UserAdd

urlpatterns = [
    path('adduser', UserAdd.as_view(), name='adduser'),
]