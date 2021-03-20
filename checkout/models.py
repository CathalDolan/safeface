import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings

from django_countries.fields import CountryField

from products.models import Product
from profiles.models import UserProfile


# This is the overall order
class Order(models.Model):

    order_number = models.CharField(max_length=32, null=False, editable=False)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True, related_name='orders')
    date = models.DateTimeField(auto_now_add=True)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    company_name = models.CharField(max_length=254, null=False, blank=False)
    department = models.CharField(max_length=254, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    county = models.CharField(max_length=80, null=True, blank=True)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    country = CountryField(blank_label='Country *', null=False, blank=False)
    products_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    delivery_cost = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    sub_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    net_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    vat = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    gross_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    original_bag = models.TextField(null=False, blank=False, default='')

    def _generate_order_number(self):
        return uuid.uuid4().hex.upper()

    def update_total(self):

        self.products_total = self.lineitems.aggregate(Sum('lineitem_total'))['lineitem_total__sum'] or 0
        if self.products_total < settings.FREE_DELIVERY_THRESHOLD:
            self.delivery_cost = settings.STANDARD_DELIVERY_PRICE
        else:
            self.delivery_cost = 0
        self.net_total = self.products_total + self.delivery_cost
        self.vat = self.net_total * settings.VAT_RATE / 100
        self.gross_total = self.net_total + self.vat
        self.save()

    def save(self, *args, **kwargs):
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


# Each individual product is given it's own line on the order form with a total cost for that line
class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems')
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
    product_colour = models.CharField(max_length=50, null=True, blank=True)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)

    def save(self, *args, **kwargs):

        if self.quantity >= self.product.qty_5:
            price = self.product.price_5
        elif self.quantity >= self.product.qty_4:
            price = self.product.price_4
        elif self.quantity >= self.product.qty_3:
            price = self.product.price_3
        elif self.quantity >= self.product.qty_2:
            price = self.product.price_2
        elif self.quantity >= self.product.qty_1:
            price = self.product.price_1
        else:
            print("else")

        self.lineitem_total = price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'SKU {self.product.sku} on order {self.order.order_number}'
