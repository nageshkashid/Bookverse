from django.urls import path
from . import views as v

urlpatterns = [
    path("history/", v.order_history, name="history"),
    path("<int:order_id>/", v.order_detail, name="detail"),
    path("checkout/<int:address_id>/", v.checkout_with_address, name="checkout_with_address"),

]
