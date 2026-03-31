from django.db import models
import uuid

class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
    

class Book(models.Model):

    CATEGORY_CHOICES = [
        ('fiction', 'Fiction'),
        ('nonfiction', 'Non-Fiction'),
        ('academic', 'Academic'),
        ('selfhelp', 'Self-Help'),
        ('biography', 'Biography'),
    ]

    isbn = models.CharField(max_length=20, unique=True, editable=False)

    title = models.CharField(max_length=200)
    author = models.CharField(max_length=150 , default="Unknown Author")
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='books/')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.isbn:
            self.isbn = f"BK-{uuid.uuid4().hex[:8].upper()}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name="Book"
        ordering = ['-created_at']
