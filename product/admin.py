from django.contrib import admin
from .models import Product, Categories, Banners, Sale_Item

# Register your models here.
admin.site.register(Categories)
admin.site.register(Banners)
admin.site.register(Product)
admin.site.register(Sale_Item)