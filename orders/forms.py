from django import forms
from .models import Order

PAYMENT_TYPE=(
    ('cod','CASH ON DELIVERY'),
    ('paypal','PAYPAL'),
)

class OrderForm(forms.ModelForm):
    payment_type = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=PAYMENT_TYPE,
        label="",
        help_text='Payment option',
        )
    
    class Meta:
        model = Order
        fields = (
            'customer_profile',
            'cart',
            'billing_address',
            'shipping_address',
            'status',
            'shipping_price',
            'order_total',
            'payment_type',
        )