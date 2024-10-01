from django.urls import path

from . import views

urlpatterns = [
    path('admin_index', views.admin_index, name="admin_index"),
    path('admin_product/', views.admin_product, name="admin_product"),
    path('admin_add_category/', views.admin_add_category, name='admin_add_category'),
    path("admin_add_category_validation/", views.admin_add_category_validation, name = "admin_add_category_validation"),
    path("admin_add_product/", views.admin_add_product, name = "admin_add_product"),
    path("admin_add_product_validation/", views.admin_add_product_validation, name = "admin_add_product_validation"),
    path('edit_product/<int:id>', views.edit_product, name='edit_product'),
    path('update/<int:id>', views.update, name='update'),
]