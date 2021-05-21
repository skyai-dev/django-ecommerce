# importing django classes and methods
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password

# importing our data models
from website.models.category import Category
from website.models.subcategory import SubCategory

def logout(request):
    request.session.clear()
    return redirect('login')


def home(request):
    # creating empty objects
    customer = None
    data = {}

    # fetching all catgory and subcategory objects
    categories = Category.get_all_categories()
    data['categories'] = categories
    data['subcategories'] = SubCategory.get_all_subcategories()

    # returning html page and fetched data
    return render(request,'home.html',data)

def about(request):
    return render(request,'about.html',{})


def blog(request):
    return render(request,'blog.html',{})

def elements(request):
    return render(request,'elements.html',{})

def portfolio_item(request):
    return render(request,'portfolio-item.html',{})

def blog_single(request):
    return render(request,'blog-single.html',{})

def shop_single(request):
    return render(request,'shop-single.html',{})

def portfolio_category(request):
    return render(request,'portfolio-category.html',{})

