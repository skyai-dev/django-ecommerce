# importing django classes and methods
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.views import View
from django.contrib.auth.hashers import check_password

# importing our data models
from website.models.customer import Customer

# definig class for Login
class Login(View):
    return_url = None
    def get(self,request):
        Login.return_url = request.GET.get('return_url')
        return render(request, 'login.html')

    def post(self,request):
        # retrieving information sent throught post method
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)

        # checking if any error occured and storing it in error_message variable
        error_message = None
        if customer:
            flag = check_password(password, customer.password)
            # copied code section start
            if flag:
                request.session['customer'] = customer.id
                request.session['customer_name'] = customer.first_name
                if Login.return_url:
                    return HttpResponseRedirect(Login.return_url)
                else:
                    Login.return_url = None
                    return redirect('home')
            else:
                error_message = "Email or password invalid"

        else:
            error_message = "Email or password invalid"

        # printing customer email and password for debugging purpose
        print(email, password)

        # returning html page along with error_message if any
        return render(request, 'login.html', {'error': error_message})
