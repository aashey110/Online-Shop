from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Product
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='/admin/login/')
def admin_index(request):
    data = {
        "active_page": 'index'

    }
    return render(request, "admin_index.html", data)

@login_required(login_url='/admin/login/')
def admin_product(request):
    all_categories = Category.objects.all()
    all_product = Product.objects.all()
    data = {
        "categories": all_categories,
        "products": all_product,
        "active_page": 'product'
    }
    return render(request, "admin_product.html", data)

@login_required(login_url='/admin/login/')
def admin_add_category(request):
    return render(request, "admin_add_category.html")



def admin_add_category_validation(request):
    category_name = request.POST['c_name']
    category_image = request.FILES['c_image']

    Category.objects.create(name=category_name, image=category_image)

    messages.success(request, "Category added Successfully")
    return redirect('admin_add_category')


@login_required(login_url='/admin/login/')
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
    

@login_required(login_url='/admin_index/login/')
def edit_product(request, id):
    pro = Product.objects.get(id=id)
    category_list = Category.objects.all()
    data = {
        "product": pro,
        "show_category": category_list
    }
    return render(request, 'edit_product.html', data)
    


def update(request, id):
    if request.method == 'POST':
        product = get_object_or_404(Product, id=id)
        
        product_name = request.POST['p_name']
        product_price = request.POST['p_price']
        product_discount = request.POST['p_discount']
        product_description = request.POST['p_description']
        product_category = request.POST['p_category']
        product_stock = request.POST['p_stock']

        if 'p_image' in request.FILES:
            product_image = request.FILES['p_image']
            product.image = product_image

        product.name = product_name
        product.price = product_price
        product.discount = product_discount
        product.description = product_description
        product.category_id = product_category
        product.stock = product_stock
        
        product.save()

        messages.success(request, "Product updated successfully")
        return redirect("admin_add_product")
    
    else:
        messages.error(request, "Invalid request method")
        return redirect("admin_add_product")



def admin_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('admin_index')
    return render(request, 'login.html')

def admin_accounts(request):
    return render(request, 'accounts.html')

#code to log out
def admin_logout(request):
    logout(request)
    return redirect('login')
