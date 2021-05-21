from django.db import models
from .category import Category
from .subcategory import SubCategory

class Product(models.Model):
    name = models.CharField(max_length=150)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,default=1,null=True,blank=True)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, default=1, null=True, blank=True)
    description = models.CharField(max_length=400, default="")
    image = models.ImageField(upload_to='uploads/products/')

    def __str__(self):
        return f"{self.name},{self.subcategory.name},{self.category.name}"

    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Product.objects.filter(category = category_id)
        else:
            return Product.get_all_products()

    @staticmethod
    def get_all_products_by_subcategory_id(subcategory_id):
        if subcategory_id:
            return Product.objects.filter(subcategory = subcategory_id)
        else:
            return Product.get_all_products()

    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter(id__in=ids)

    @staticmethod
    def get_product_by_exact_id(id):
        return Product.objects.get(id=id)