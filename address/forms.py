from django import forms
from django_countries.fields import CountryField

from .models import BillingAddress, ShippingAddress

class BillingAddressForm(forms.ModelForm):
    country                     = CountryField(blank_label='(Select country)').formfield()
    same_as_shipping_address    = forms.BooleanField(
                                    required=False,
                                    widget=forms.CheckboxInput()
                                    )
    save_for_next_time          = forms.BooleanField(
                                    required=False,
                                    widget=forms.CheckboxInput()
                                )
    class Meta:
        model = BillingAddress
        fields = (
            'house_number' ,
            'street',
            'barangay',
            'city',
            'province', 
            'zip_code',
            'country',
        )

class ShippingAddressForm(forms.ModelForm):
    country = CountryField(blank_label='(Select country)').formfield()
    class Meta:
        model = ShippingAddress
        fields = (
            'house_number' ,
            'street',
            'barangay',
            'city',
            'province', 
            'zip_code',
            'country',
        )
