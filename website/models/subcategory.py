from django.db import models
from .category import Category

class SubCategory(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1, null=True, blank=True)

    def __str__(self):
        return f"{self.name}"


    @staticmethod
    def get_all_subcategories():
        return SubCategory.objects.all()


    @staticmethod
    def get_all_subcategory_by_categoryid(category_id):
        if category_id:
            print("Get all subcategory by category id ran")
            return SubCategory.objects.filter(category = category_id)
        else:
            return SubCategory.get_all_subcategories()