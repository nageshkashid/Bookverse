

from .import views as v
from django.urls import path

urlpatterns = [
    path('',v.home , name='home'),
]
