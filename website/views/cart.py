# importing django classes and methods
from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password

# importing our data models
from website.models.category import Category
from website.models.subcategory import SubCategory
from website.models.product import Product
from website.models.customer import Customer
from website.models.orders import Order


class Cart(View):
    def get(self,request):
        ids = list(request.session.get('cart').keys())
        if ids:
            print("ids fetched from products in cart")
        products = Product.get_products_by_id(ids)
        if products:
            print(products)
        return render(request, 'cart.html', {'products': products})
