from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'category', 'activate')  # Columns shown in list view
    search_fields = ('name',)  # Add search box
    list_filter = ('category',)  # Add filter sidebar
