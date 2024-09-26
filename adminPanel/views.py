from django.shortcuts import render, redirect
from .models import Category, Product
from django.contrib import messages

# Create your views here.
def admin_panel(request):
    return render(request, "admin_panel.html")


def admin_product(request):
    all_categories = Category.objects.all()
    all_product = Product.objects.all()
    data = {
        "categories": all_categories,
        "products": all_product,
        "active_page": 'product'
    }
    return render(request, "admin_product.html", data)


def admin_add_category(request):
    return render(request, "admin_add_category.html")

def admin_add_category_validation(request):
    category_name = request.POST['c_name']
    category_image = request.FILES['c_image']

    Category.objects.create(name=category_name, image=category_image)

    messages.success(request, "Category added Successfully")

    return redirect('admin_add_category')

def admin_add_product(request):
    category_list = Category.objects.all()

    return render(request, "admin_add_product.html", {"show_category":category_list} )

def admin_add_product_validation(request):
    if request.POST:
        product_name = request.POST['p_name']
        product_price = request.POST['p_price']
        product_discount = request.POST['p_discount']
        product_image = request.FILES['p_image']
        product_description = request.POST['p_description']
        product_category = request.POST['p_category']
        product_stock = request.POST['p_stock']
        
        Product.objects.create(name=product_name, price=product_price, discount=product_discount, image= product_image, description=product_description, category_id=product_category, stock=product_stock)

        messages.success(request, "Product added Successfully")


        return redirect("admin_add_product")