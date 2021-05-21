from django.db import models
from .product import Product

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,default=1,null=True,blank=True)
    review = models.CharField(max_length=400)
    name = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return f"{self.name} {self.email}"

    def saveReview(self):
        self.save()

    @staticmethod
    def get_review_by_product_id(id):
        try:
            return Review.objects.filter(product=id)
        except:
            return False
