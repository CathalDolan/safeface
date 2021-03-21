from django.contrib import admin
from .models import Order, OrderLineItem


# Allows us to manipulate the line
class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):

    # Comes from the class above
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'date',
                       'products_total', 'delivery_cost',
                       'net_total', 'vat', 'gross_total',)

    fields = ('order_number', 'date', 'full_name',
              'company_name', 'department', 'email',
              'phone_number', 'street_address1',
              'street_address2', 'town_or_city',
              'county', 'postcode', 'country',
              'products_total', 'delivery_cost',
              'net_total', 'vat', 'gross_total',
              'original_cart', 'stripe_pid',)

    list_display = ('order_number', 'date', 'full_name',
                    'company_name', 'net_total', 'vat',
                    'gross_total',)

    ordering = ('-date',)

admin.site.register(Order, OrderAdmin)
