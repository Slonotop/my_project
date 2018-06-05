from django import forms
from .models import *
from django.forms import ModelForm, CharField


class CheckoutContactForm(forms.Form):
    name = forms.CharField(required=True)
    phone = forms.CharField(required=True)


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer_name', 'customer_phone']

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['name'].widget.attrs.update({'class': 'form-control'})
    #     self.fields['phone'].widget.attrs.update({'class': 'form-control'})