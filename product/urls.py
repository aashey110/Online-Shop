from django.urls import path
from . import views

urlpatterns = [
    path('products', views.products, name = "product"),
    path('categories/', views.categories, name = "categories"),
    path('product-details/<int:id>/', views.productDetail, name = "productdetail"),
    path('product_by_category/<int:category_id>/', views.product_by_category, name="product_by_category"),
]