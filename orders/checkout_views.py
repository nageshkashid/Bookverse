from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from cart.models import Cart
from accounts.models import Address

@login_required
def checkout(request):
    cart = request.user.cart
    addresses = request.user.addresses.all()

    if cart.items.count() == 0:
        return redirect("cart:view")

    return render(request, "orders/checkout.html", {
        "cart": cart,
        "addresses": addresses
    })