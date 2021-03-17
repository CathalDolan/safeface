from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('full_name', 'email', 'phone_number',
                  'company_name', 'department',
                  'street_address1', 'street_address2',
                  'town_or_city', 'county', 'postcode',
                  'country',)

    # Overrides the default form labels, sets...
    # ...autofocus, and puts * on required fields
    def __init__(self, *args, **kwargs):

        # Calls the default form set-up
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'company_name': 'Company Name',
            'department': 'Department',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'town_or_city': 'Town or City',
            'county': 'County / State / Locality',
            'postcode': 'Postal Code / Zip',
        }

        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
                self.fields[field].widget.attrs['class'] = 'stripe-style-input'
                self.fields[field].label = False
