from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class Categories(models.Model):
    name = models.CharField(max_length=100) 
    image = models.ImageField(upload_to='categories/images/', null = True)

    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    name = models.CharField(max_length = 2000)
    price = models.IntegerField()
    discount = models.IntegerField()
    image = models.ImageField(upload_to='products/images/', null = True, max_length=250, default=None)
    description = models.TextField()
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, related_name="products")

    def __str__(self)  -> str:
        return self.name
    
class Banners(models.Model):
    banner_image = models.ImageField(upload_to='banners/images/', null = True)
    
class Sale_Item(models.Model):
    name = models.CharField(max_length = 2000)
    price = models.IntegerField()
    discount = models.IntegerField()
    image = models.ImageField(upload_to='products/images/', null = True)
    description = models.TextField()
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    def __str__(self)  -> str:
        return self.name
