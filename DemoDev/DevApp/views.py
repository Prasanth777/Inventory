from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import auth
from .models import Account, Inventory, Images
from django.http import HttpResponse
from django.contrib import messages
from .forms import InventoryForm,ImagesForm
from django.forms import modelformset_factory
import os.path
from django.core.files.base import ContentFile

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Create your views here.
def login(request):
    if request.method == 'POST':
        email = request.POST['login_email']
        password1 = request.POST['login_pass']
        user = auth.authenticate(username=email,password=password1)
        if user is not None:
            auth.login(request,user)
            user_id = request.user.id
            if request.user.is_admin is False:
                return redirect('gallery_with_pk',id=user_id)
            else:
                return redirect('gallery_admin_with_pk',id=user_id)
        else:
            messages.info(request,'Invalid Credentials!!')
            return redirect('login')
    else:
        return render(request, 'DevApp/home.html')

def register(request):
    if request.method == 'POST':
        company_name = request.POST['register_cname']
        first_name = request.POST['register_fname']
        last_name = request.POST['register_lname']
        email = request.POST['register_email']
        password1 = request.POST['register_pwd']
        password2 = request.POST['register_confpwd']
        if password1==password2:
            if Account.objects.filter(email=email).exists():
                messages.warning(request,"Email ID already Exists")
                return redirect('register')
            else:
                user = Account.objects.create_user(email=email,companyname=company_name,firstname=first_name,lastname=last_name,password=password1)
                user.save();
                messages.info(request,"User created")
                return redirect('/')
        else:
            messages.error(request,"Password not matching")
            return redirect('register')
    return render(request,'DevApp/register.html/')


def logout(request):
    auth.logout(request)
    return redirect('login')

def gallery_admin(request,id=None):
    if request.user.is_authenticated:
        if request.method == 'GET':
            #Images_dict={}
            #User = get_object_or_404(Account,id=id)
            Inventorys = Inventory.objects.all()
            Accounts = Account.objects.all()
            #for item in Inventorys:
                #Images_dict[item] = Images.objects.filter(inv_id=item.id)
            #Images_dict = Images.objects.filter(inv__id=Inventorys.id)
            return render(request,'DevApp/gallery.html',{'Inventory_Images':Inventorys,'Accounts':Accounts})
    else:
        return redirect('login')

def gallery_filter(request):
    if request.method == 'GET':
        Inventorys = None
        Accounts = Account.objects.all()
        if not request.GET['company'] and not request.GET['category'] and not request.GET['color']:
            Inventorys = Inventory.objects.filter(category=None, color=None)

        if request.GET['company'] and request.GET['category'] and request.GET['color']:
            company=request.GET['company']
            category = request.GET['category']
            color = request.GET['color']
            print(company)
            print(category)
            print(color)
            for a in Accounts:
                if a.companyname == company:
                    Inventorys = Inventory.objects.filter(owner=a,category=category,color=color)

        elif request.GET['category'] and request.GET['color']:
            color = request.GET['color']
            category = request.GET['category']
            print(category)
            print(color)
            Inventorys = Inventory.objects.filter(category=category,color=color)

        elif request.GET['company'] and request.GET['category']:
            company=request.GET['company']
            category = request.GET['category']
            print(company)
            print(category)
            for a in Accounts:
                if a.companyname == company:
                    Inventorys = Inventory.objects.filter(owner=a,category=category)

        elif request.GET['company'] and request.GET['color']:
            company=request.GET['company']
            color = request.GET['color']
            print(company)
            print(color)
            for a in Accounts:
                if a.companyname == company:
                    Inventorys = Inventory.objects.filter(owner=a,color=color)

        elif request.GET['company']:
            company=request.GET['company']
            print(company)
            for a in Accounts:
                if a.companyname == company:
                    Inventorys = Inventory.objects.filter(owner=a)

        elif request.GET['category']:
            category=request.GET['category']
            print(category)
            Inventorys = Inventory.objects.filter(category=category)

        elif request.GET['color']:
            color=request.GET['color']
            print(color)
            Inventorys = Inventory.objects.filter(color=color)



        return render(request, 'DevApp/gallery.html', {'Inventory_Images': Inventorys, 'Accounts': Accounts})

def gallery(request,id=None):
    if request.user.is_authenticated:
        if request.method == 'GET':
            #Images_dict={}
            #User = get_object_or_404(Account,id=id)
            Inventorys = Inventory.objects.filter(owner=request.user)
            #for item in Inventorys:
            #    Images_dict[item] = Images.objects.filter(inv_id=item.id)
            #Images_dict = Images.objects.filter(inv__id=Inventorys.id)
            return render(request,'DevApp/gallery.html',{'Inventory_Images':Inventorys})
    else:
        return redirect('login')

def gallery_details(request,id1=None,id2=None):
    if request.user.is_authenticated:
        if request.method == 'GET':

            #User = get_object_or_404(Account,id=id)
            Images_dict = Images.objects.filter(inv_id=id2)

            #Images_dict = Images.objects.filter(inv__id=Inventorys.id)
            return render(request,'DevApp/details.html',{'Inventory_Images':Images_dict,'Images_d':Images_dict})
    else:
        return redirect('login')

def thumbnail_change(request,id=None):
    if request.method == 'POST':
        thumb = get_object_or_404(Images,id=id)
        #copy = ContentFile(thumb.image.read())
        #new_name = thumb.image.name.split("/")[-1]
        thumb.inv.image.save(thumb.image.name.split("/")[-1],ContentFile(thumb.image.read()))
        #thumb.inv.image.save()
        print("Thumbnail changed")
        return redirect('gallery_admin_with_pk',id=request.user.id)

def delete_inventory(request,id):
    if request.method == 'POST':
        invent = get_object_or_404(Inventory,id=id)
        im = Images.objects.filter(inv=invent)
        for i in im:
            i.delete()
        invent.delete()
        if request.user.is_admin is False:
            return redirect('gallery_with_pk',id=request.user.id)
        else:
            return redirect('gallery_admin_with_pk', id=request.user.id)

def upload_image(request):
    if request.method == 'POST':
        files = request.FILES.getlist('image')
        form = InventoryForm(request.POST or None, request.FILES or None)
        #form2 = ImagesForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            inv = form.save(commit=False)
            inv.owner = request.user
            inv.save()
            for f in files:
                try:
                    invent = Images(inv=inv,image=f)
                    invent.save()

                except Exception as e:
                    break
            print("Form saved")
            if request.user.is_admin is False:
                return redirect('gallery_with_pk', id=request.user.id)
            else:
                return redirect('gallery_admin_with_pk', id=request.user.id)
    else:
        form = InventoryForm()


    return render(request,'DevApp/upload.html',{'form':form})

def delete_image(request,pk):
    invent = get_object_or_404(Inventory, pk=pk)
    try:
        if request.method == 'POST':
            form=InventoryForm(request.POST,instance=invent)
            invent.delete()
            messages.success(request,'You have successfully deleted the post')
            print("deleted")

        else:
            form = InventoryForm(instance=invent)
    except Exception as e:
        messages.warning(request,'The post could not be deleted.Error:{}'.format(str(e)))
    context={'form':form,'invent':invent}
    return render(request,"DevApp/gallery.html",context)

def class_change(request,id):
    if request.method == "POST":
        change = get_object_or_404(Inventory,id=id)
        cat = request.POST.get('category',None)
        clr = request.POST.get('color',None)
        print(cat)
        print(clr)
        change.category = cat
        change.color = clr
        change.save()
        print("Category or Color changed")
        return redirect('gallery_admin_with_pk', id=request.user.id)




