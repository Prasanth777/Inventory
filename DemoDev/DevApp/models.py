from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager

from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile
# Create your models here.

class MyAccountManager(BaseUserManager):
    def create_user(self,email,companyname,firstname,lastname,password=None):
        if not email:
            raise ValueError("User must have an email address")
        if not companyname:
            raise ValueError("User must have an company name")
        if not password:
            raise ValueError("User must have a password")
        user = self.model(
            email=self.normalize_email(email),
            companyname=companyname,
            firstname=firstname,
            lastname=lastname,
            )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email,companyname,firstname,lastname,password):
        user = self.create_user(
            email = self.normalize_email(email),
            companyname=companyname,
            firstname=firstname,
            lastname=lastname,
            password=password,
            )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using = self._db)
        return user


class Account(AbstractBaseUser):

    email = models.EmailField(verbose_name="email", unique=True,max_length=60)
    pass1 = models.CharField(max_length=30)
    pass2 = models.CharField(max_length=30)
    date_joined = models.DateTimeField(verbose_name="date joined",auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login",auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    companyname = models.CharField(blank=True,max_length=30,null=True)
    firstname = models.CharField(blank=True,max_length=30,null=True)
    lastname = models.CharField(blank=True,max_length=30,null=True)

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = ['companyname','firstname','lastname']

    objects = MyAccountManager()
    def __str__(self):
        return self.companyname

    def has_perm(self,perm,obj=None):
        return self.is_admin
    def has_module_perms(self,app_label):
        return True

class Inventory(models.Model):
    brand = models.CharField(max_length=50,null=True,blank=True)
    width = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True,auto_now=False)
    image = models.FileField(upload_to='Image/',null=True)
    category = models.CharField(max_length=50,null=True,blank=True,default=None)
    color = models.CharField(max_length=50,null=True,blank=True,default=None)
    price = models.CharField(max_length=50,null=True,blank=True,default=None)
    owner= models.ForeignKey(Account,on_delete=models.CASCADE)

    def delete(self, *args,**kwargs):
        self.image.delete()
        super().delete(*args,**kwargs)

    def __str__(self):
        return self.brand

    class Meta:
        ordering = ["-timestamp"]

class Orders(models.Model):
    ord = models.ForeignKey(Account, on_delete=models.CASCADE)
    image = models.FileField(upload_to='Image/', null=True)
    name = models.CharField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=20,null=True,blank=True)
    price = models.CharField(max_length=10,null=True,blank=True)
    delivery = models.CharField(max_length=10,null=True,blank=True)
    time = models.CharField(max_length=10,null=True,blank=True)
    address= models.CharField(max_length=100,null=True,blank=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    client = models.CharField(max_length=20,null=True,blank=True)
    available = models.BooleanField(default=False)
    def delete(self, *args,**kwargs):
        self.image.delete()
        super().delete(*args,**kwargs)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-timestamp"]

class Flips(models.Model):
    flip = models.ForeignKey(Orders, on_delete=models.CASCADE)
    image = models.FileField(upload_to='Image/', null=True)
    brand = models.CharField(max_length=50, null=True, blank=True)
    def delete(self, *args,**kwargs):
        self.image.delete()
        super().delete(*args,**kwargs)

    def __str__(self):
        return self.flip.name

class Order_Image(models.Model):
    ordimg = models.ForeignKey(Orders, on_delete=models.CASCADE)
    image = models.FileField(upload_to='Image/')

    def delete(self, *args, **kwargs):
        self.image.delete()
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.ordimg.name

class Flip_Image(models.Model):
    flipimg = models.ForeignKey(Flips, on_delete=models.CASCADE)
    image = models.FileField(upload_to='Image/')

    def delete(self, *args, **kwargs):
        self.image.delete()
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.flipimg.flip.name

class Images(models.Model):
    inv = models.ForeignKey(Inventory,on_delete=models.CASCADE)
    image = models.FileField(upload_to='Image/')
    def delete(self, *args,**kwargs):
        self.image.delete()
        super().delete(*args,**kwargs)
    def __str__(self):
        return self.inv.brand




