from django.urls import path
from . import views

urlpatterns = [
    path('', views.guess_flag, name='guess_flag'),
]