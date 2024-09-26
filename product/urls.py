from django.urls import path
from . import views

urlpatterns = [
    path('products', views.products, name = "product"),
    path('categories/', views.categories, name = "categories"),
    path('product-details/<int:id>/', views.productDetail, name = "productdetail"),
    # path("add_product/", views.add_product, name = "add_product"),
    # path("add_product_validation/", views.add_product_validation, name = "add_product_validation"),
    # path("add_category/", views.add_category, name = "add_category"),
    # path("add_category_validation/", views.add_category_validation, name = "add_category_validation"),
]