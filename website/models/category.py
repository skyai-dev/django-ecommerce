from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='uploads/category/')

    def __str__(self):
        return f"{self.name}"

    @staticmethod
    def get_all_categories():
        return Category.objects.all()