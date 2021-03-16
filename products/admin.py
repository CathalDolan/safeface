from django.contrib import admin
from .models import Product, Category


# Register your models here.

# Order of the products in Admin
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'friendly_name',
        'name',
        'category',
        'image1',
        'image2',
        'image3',
    )

    # Sorted 1-9 by SKU
    ordering = ('sku',)


# Order of teh Categories in Admin
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
