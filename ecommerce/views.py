from django.shortcuts import render
from product.models import Banners, Sale_Item, Product

def index(request):
    all_banners = Banners.objects.all()
    sale_items = Sale_Item.objects.all()
    product = Product.objects.all()
    data = {
        "title" : 'Home',
        "banner": all_banners,
        "sale_items": sale_items,
        "products": product,
    }
    return render(request, 'index.html', data)

def about(request):
    data = {
        "title": 'About'
    }
    return render(request, 'about.html', data)

def category(request):
    data = {
        "title": 'Category'
    }
    return render(request, 'category.html', data)

def contact_us(request):
    data = {
        "title": 'Contact'
    }
    return render(request, 'contact_us.html', data)