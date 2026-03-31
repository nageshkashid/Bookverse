from .models import Book
from django.shortcuts import render, get_object_or_404
from django.db import models


def book_list(request):
    search = request.GET.get("search", "")
    category = request.GET.get("category", "")

    books = Book.objects.all()

    if search:
        books = books.filter(
            models.Q(title__icontains=search) |
            models.Q(author__icontains=search) |
            models.Q(isbn__icontains=search)
        )

    if category:
        books = books.filter(category=category)

    context = {
        "books": books.order_by("-created_at"),
        "categories": Book.CATEGORY_CHOICES,
    }
    return render(request, "user/book_list.html", context)



def book_detail(request, isbn):
    book = get_object_or_404(Book, isbn=isbn)
    return render(request, "user/book_detail.html", {"book": book})






