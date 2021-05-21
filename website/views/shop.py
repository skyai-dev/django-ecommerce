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

class Shop(View):
    def get(self, request):
        # fetching all products from database
        products = None
        products = Product.get_all_products()
        categories = Category.get_all_categories()

        # storing fetched products in dictionary object data
        data = {}
        data['products'] = products
        data['categories'] = categories

        # Chekcing if cart exists or not
        if request.session.get('cart'):
            pass
        else:
            cart = {}
            request.session['cart'] = cart

        # rendering shop.html page with all the products in data dictionary object
        return render(request, 'shop.html', data)

    def post(self, request):
        # code for adding product in the cart
        cart=request.session.get('cart')
        remove = request.POST.get('remove')
        product = request.POST.get('product')
        if cart and product:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if cart[product] <= 1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity - 1
                else:
                    cart[product] = quantity + 1
            else:
                cart[product] = 1
        elif product:
            cart = {}
            cart[product] = 1

        if cart:
            request.session['cart'] = cart
        print("Cart : ", cart)

        # code for displaying categories and subcategories in navbar
        data = {}
        categories = Category.get_all_categories()
        subcategories = SubCategory.get_all_subcategories()
        data['categories'] = categories
        data['subcategories'] = subcategories

        # code for displaying products
        products = None
        category_id = request.POST.get('category_id')
        subcategory_id = request.POST.get('subcategory_id')
        if category_id:
            products = Product.get_all_products_by_categoryid(category_id)
            data['category_id'] = category_id
        elif subcategory_id:
            products = Product.get_all_products_by_subcategory_id(subcategory_id)
            data['subcategory_id'] = subcategory_id
        else:
            products = Product.get_all_products()
        data['products'] = products

        # rendering shop.html page with all products stored in data dictionary object
        return render(request, 'shop.html', data)
