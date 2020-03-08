from django import forms
from django.forms import ModelForm
from .models import Inventory
class InventoryForm(ModelForm):
    image = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True,'class' : 'upload'}))


    class Meta:
        model=Inventory
        fields=[
            "image",
            "brand",
            "price",

        ]
