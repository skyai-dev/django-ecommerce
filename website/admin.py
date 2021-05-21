from website.models.review import Review
from django.contrib import admin
from .models.category import Category
from .models.subcategory import SubCategory
from .models.product import Product
from .models.customer import Customer
from .models.orders import Order
from .models.mail import Mail

# Register your models here.

admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Mail)
admin.site.register(Review)