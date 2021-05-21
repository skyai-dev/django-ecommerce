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


class SignUp(View):
    def get(self,request):
        return render(request, 'signup.html')

    def post(self,request):
        # retrieving information sent throught post method from signup.html page
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')

        # storing retrieved information in the dictionary object value
        value = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email
        }

        # creating a customer object and initializing its data members
        customer = Customer(first_name=first_name,
                            last_name=last_name,
                            phone=phone,
                            email=email,
                            password=password)

        # checking if retrieved information was correct and storing error msg accordingly
        error_message = None
        error_message = self.validateCustomer(customer)

        # if noting stored in error_message then hasing the customer password
        # storing customer data storing it in databse and redirecting ourselve to home page
        # else we return error message and values entered by the customer
        # to signup.html page
        if not error_message:
            customer.password = make_password(customer.password)
            customer.register()
            return redirect('home')
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render(request, 'signup.html', data)

    def validateCustomer(self,customer):
        # producing error message according to errror occured
        error_message = None
        if (not customer.first_name):
            error_message = 'First Name Required !!'
        elif len(customer.first_name) < 4:
            error_message = "First Name Must be 4 char long"
        elif (not customer.last_name):
            error_message = 'Last Name Required !!'
        elif len(customer.last_name) < 4:
            error_message = "Last Name Must be 4 char long"
        elif (not customer.phone):
            error_message = 'Phone Number Required !!'
        elif len(customer.phone) < 10:
            error_message = "Phone Number must be 10 digits long"
        elif (not customer.email):
            error_message = 'Email Required !!'
        elif (not customer.password):
            error_message = "Password Required"
        elif len(customer.password) < 8:
            error_message = "Minimum password length must be 8 characters"
        elif customer.isExists():  # checks if email already used by some other customer
            error_message = "Email address already registered.."

        # returning error_message to called function
        return error_message

