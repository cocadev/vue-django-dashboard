from django import forms
from .models import *


class ProductPriceForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProductPriceForm, self).__init__(*args, **kwargs)
        self.fields['price'].required = True
        self.fields['units'].required = True

    def save(self, commit=True):
        price = super(ProductPriceForm, self).save(commit=False)

        if commit:
            price.save()

        return price

    class Meta:
        model = ProductPrice
        fields = ('product', 'price', 'units', 'description')
