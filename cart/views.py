from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from books.models import Book
from .models import Cart, CartItem

@login_required
def cart_view(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    return render(request, "cart/cart_view.html", {"cart": cart})


@login_required
def add_to_cart(request, isbn):
    cart, created = Cart.objects.get_or_create(user=request.user)
    book = get_object_or_404(Book, isbn=isbn)

    item, created = CartItem.objects.get_or_create(cart=cart, book=book)

    if not created:
        item.quantity += 1
    
    item.save()
    return redirect("cart:view")


@login_required
def remove_item(request, isbn):
    cart = request.user.cart
    book = get_object_or_404(Book, isbn=isbn)
    CartItem.objects.filter(cart=cart, book=book).delete()
    return redirect("cart:view")


@login_required
def clear_cart(request):
    request.user.cart.items.all().delete()
    return redirect("cart:view")


@login_required
def increase_qty(request, isbn):
    cart = request.user.cart
    item = get_object_or_404(CartItem, cart=cart, book__isbn=isbn)
    item.quantity += 1
    item.save()
    return redirect("cart:view")


@login_required
def decrease_qty(request, isbn):
    cart = request.user.cart
    item = get_object_or_404(CartItem, cart=cart, book__isbn=isbn)

    if item.quantity > 1:
        item.quantity -= 1
        item.save()
    else:
        item.delete()

    return redirect("cart:view")



# Create your views here.
