"""
URL configuration for bookverse project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path 
from . import views as v

urlpatterns = [
    path("", v.cart_view, name="view"),
    path("add/<str:isbn>/", v.add_to_cart, name="add"),
    path("remove/<str:isbn>/", v.remove_item, name="remove"),
    path("increase/<str:isbn>/", v.increase_qty, name="increase"),
    path("decrease/<str:isbn>/", v.decrease_qty, name="decrease"),
    path("clear/", v.clear_cart, name="clear"),
]

