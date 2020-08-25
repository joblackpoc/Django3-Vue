from django.shortcuts import render
from store.models import Product, Category

def Frontpage(request):
    products = Product.objects.filter(is_featured=True)

    context = {
        'products':products
        }

    return render(request,'frontpage.html',context)

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')