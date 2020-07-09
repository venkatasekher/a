from App8.models import ProductModel
from django import forms


class ProductForm(forms.ModelForm):
    pno = forms.IntegerField(min_value=1001)

    class Meta:
        fields = '__all__'
        model = ProductModel

    def clean_price(self):
        price = self.cleaned_data['price']
        if price >= 1000:
            return price
        else:
            raise forms.ValidationError('Price must be 1000 or Abvoe')

    def clean_quantity(self):
        qty=self.cleaned_data['quantity']
        if qty >0:
            return qty
        else:
            raise forms.ValidationError('Quantity Must Not be 0 ')

