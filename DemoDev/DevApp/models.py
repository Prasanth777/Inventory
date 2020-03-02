from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager




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
        return self.email

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
    price = models.IntegerField(null=False,blank=False)
    owner= models.ForeignKey(Account,on_delete=models.CASCADE)

    def delete(self, *args,**kwargs):
        self.image.delete()
        super().delete(*args,**kwargs)

    def __str__(self):
        return self.brand

    class Meta:
        ordering = ["-timestamp"]

class Images(models.Model):
    inv = models.ForeignKey(Inventory,on_delete=models.CASCADE)
    image = models.FileField(upload_to='Image/')
    def delete(self, *args,**kwargs):
        self.image.delete()
        super().delete(*args,**kwargs)
    def __str__(self):
        return self.inv.brand