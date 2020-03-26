from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account,Inventory,Images,Orders,Order_Image,Flip_Image,Flips


# Register your models here.
class AccountAdmin(admin.ModelAdmin):
    class Meta:
        model = Account
    list_display = ('email','companyname','firstname','lastname','date_joined','last_login','is_admin','is_staff')
    search_fields = ('email','companyname','firstname','lastname','pass1')
    readonly_fields = ('date_joined','last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = (
        (None, {'fields':('email','password')}),
        ('Personal Info',{'fields':('companyname','firstname','lastname','pass1','pass2')}),
        ('Additional Info',{'fields':('date_joined','last_login','is_admin','is_staff')})
    )
class InventoryAdmin(admin.ModelAdmin):
    list_display = ["owner","brand","timestamp"]

class ImagesAdmin(admin.ModelAdmin):
    list_display = ["inv","image"]

class OrdersAdmin(admin.ModelAdmin):
    list_display = ["ord","name","timestamp"]

class Orders_ImagesAdmin(admin.ModelAdmin):
    list_display = ["ordimg"]

class Flip_ImagesAdmin(admin.ModelAdmin):
    list_display = ["flipimg"]

class FlipsAdmin(admin.ModelAdmin):
    list_display = ["flip","brand"]

admin.site.register(Account,AccountAdmin)
admin.site.register(Inventory,InventoryAdmin)
admin.site.register(Images,ImagesAdmin)
admin.site.register(Orders,OrdersAdmin)
admin.site.register(Order_Image,Orders_ImagesAdmin)
admin.site.register(Flip_Image,Flip_ImagesAdmin)
admin.site.register(Flips,FlipsAdmin)
