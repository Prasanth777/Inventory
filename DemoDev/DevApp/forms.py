from django import forms
from django.forms import ModelForm
from .models import Inventory,Orders,Account,Flips


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

class FlipForm(ModelForm):
    image = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True, 'class': 'upload'}))
    brand = forms.CharField(widget=forms.TextInput(attrs={'class': 'brand'}))
    class Meta:
        model=Flips
        fields=[
            "image",
            "brand",

        ]
Acc = Account.objects.all()
Company_choice=[]
tup=()
for a in Acc:
    tup=(a.companyname,a.companyname)
    Company_choice.append(tup)


class OrderForm(ModelForm):
    image = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True, 'class': 'upload'}), label_suffix='')
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'price'}), label_suffix='')
    phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'price'}), label_suffix='')
    price = forms.CharField(widget=forms.TextInput(attrs={'class': 'price'}), label_suffix='')
    delivery = forms.CharField(label="Del",widget=forms.TextInput(attrs={'class': 'price'}), label_suffix='')
    time = forms.CharField(widget=forms.TextInput(attrs={'class': 'price'}), label_suffix='')
    address = forms.CharField(label="Addr",widget=forms.TextInput(attrs={'class': 'price'}), label_suffix='')
    client = forms.CharField(label="Comp:",widget=forms.Select(choices=Company_choice), label_suffix='')
    class Meta:
        model=Orders
        fields=[
            "image",
            "name",
             "phone",
            "price",
            "delivery",
            "time",
            "address",
           "client",
        ]