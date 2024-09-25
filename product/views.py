from django.shortcuts import render, redirect
from .models import Categories, Product
from django.contrib import messages

# Create your views here.
def products(request):
    all_products = Product.objects.all()
    data = {
        "title" : 'Products',
        "products" : all_products,
    }
    
    return render(request, "product.html", data)


def categories(request):
    all_categories = Categories.objects.all()
    data = {
        "title" : 'Categories',
        "categories": all_categories,
    }
    return render(request, "category.html", data)

def productDetail(request, id):
    single_product = Product.objects.filter(id = id)
    all_products = Product.objects.all()

    data = {
        "product" : single_product,
        "products" : all_products,
    }
    return render(request, "single_product.html", data)


def add_product(request):
    category_list = Categories.objects.all()

    return render(request, "add_product.html", {"show_category":category_list} )

def add_product_validation(request):
    if request.POST:
        product_name = request.POST['p_name']
        product_price = request.POST['p_price']
        product_discount = request.POST['p_discount']
        product_image = request.FILES['p_image']
        product_description = request.POST['p_description']
        product_category = request.POST['p_category']
        Product.objects.create(name=product_name, price=product_price, discount=product_discount, image= product_image,  description=product_description, category_id=product_category)

        messages.success(request, "Product added Successfully")


        return redirect("add_product")
    

def add_category(request):
    return render(request, "add_category.html")

def add_category_validation(request):
    category_name = request.POST['c_name']
    category_image = request.FILES['c_image']

    Categories.objects.create(name=category_name, image=category_image)

    messages.success(request, "Category added Successfully")

    return redirect('categories')
