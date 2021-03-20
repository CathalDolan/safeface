from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)

    # Overrides the default form labels, sets...
    # ...autofocus, and puts * on required fields
    def __init__(self, *args, **kwargs):

        # Calls the default form set-up
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_company_name': 'Company Name',
            'default_department': 'Department',
            'default_phone_number': 'Phone Number',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_town_or_city': 'Town or City',
            'default_county': 'County / State / Locality',
            'default_postcode': 'Postal Code / Zip',
        }

        self.fields['default_company_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'default_country':
                if self.fields[field].required:
                    print('field', field)
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'rounded-0 profile-form-input'
            self.fields[field].label = False
