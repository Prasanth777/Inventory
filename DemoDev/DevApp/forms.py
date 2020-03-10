from django import forms
from django.forms import ModelForm
from .models import Inventory
class InventoryForm(ModelForm):
    image = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True,'class' : 'upload'}))
    brand = forms.CharField(widget=forms.TextInput(attrs={'class':'brand','id':'brand'}))
    price = forms.CharField(widget=forms.TextInput(attrs={'class':'price','id':'price'}))

    class Meta:
        model=Inventory
        fields=[
            "image",
            "brand",
            "price",

        ]
