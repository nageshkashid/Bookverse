from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Order , OrderItem
from cart.models import Cart
from accounts.models import Address


@login_required
def checkout_with_address(request, address_id):
    address = get_object_or_404(Address, id=address_id, user=request.user)
    cart = Cart.objects.get(user=request.user)

    order = Order.objects.create(
        user=request.user,
        total_amount=cart.total,
        address=address,
    )

    for item in cart.items.all():
        OrderItem.objects.create(
            order=order,
            book=item.book,
            price=item.book.price,
            quantity=item.quantity,
        )

    cart.items.all().delete()
    return redirect("orders:detail", order_id=order.id)


@login_required
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, "orders/order_detail.html", {"order": order})


@login_required
def order_history(request):
    orders = request.user.orders.all().order_by("-created_at")
    return render(request, "orders/order_history.html", {"orders": orders})





