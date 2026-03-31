

from .import views as v
from django.urls import path

urlpatterns = [

    path('',v.book_list, name='book_list'),
    path('<str:isbn>/', v.book_detail, name='book_detail'),
    
]
