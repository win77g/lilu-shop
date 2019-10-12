from django import forms
from .models import *

class CheckoutContactForm(forms.Form):
    surname = forms.CharField(required=True)
    name = forms.CharField(required=True)
    phone = forms.CharField(required=True)
    email = forms.CharField(widget=forms.EmailInput({'placeholder': 'example@mail.ru', 'autocomplete': 'on'})
                            , max_length=30, )
    city = forms.CharField(required=True)
    street = forms.CharField(required=True)
    text = forms.CharField(required=True)
class CartForm(forms.Form):
    # name = forms.CharField(required=True)
    # phone = forms.CharField(required=True)
    nmb = forms.CharField(required=True)



