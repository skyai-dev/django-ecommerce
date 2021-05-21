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

class OrderView(View):
    def get(self,request):
        customer = request.session.get('customer')
        orders = Order.get_orders_by_customer(customer)
        print('Orders:',orders)
        return render(request, 'orders.html',{'orders':orders})
