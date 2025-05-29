from django.db import models

class Product(models.Model):
    class Category(models.TextChoices):
        ELECTRONICS = 'EL', 'Electronics'
        CLOTHING = 'CL', 'Clothing'
        BOOKS = 'BK', 'Books'
        TOYS = 'TY', 'Toys'

    name = models.CharField(max_length=200, blank=False, null=False)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    stock = models.BooleanField(default=False)
    category = models.CharField(
        max_length=2,
        choices=Category.choices,
        default=Category.ELECTRONICS,
    )
    image = models.ImageField(null=True, blank=True)
    activate = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.name} ({self.get_category_display()})"
