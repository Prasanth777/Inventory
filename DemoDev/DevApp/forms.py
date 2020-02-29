from django import forms
from django.forms import ModelForm
from .models import Inventory,Images
class InventoryForm(ModelForm):
    image = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    class Meta:
        model=Inventory
        fields=[
            "image",
            "brand",
            "price",

        ]

class ImagesForm(ModelForm):
    image = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    class Meta:
        model=Images
        fields=[
            "image",
        ]