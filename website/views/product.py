# importing django classes and methods
from django.shortcuts import render, redirect
from django.views import View

# importing our data models
from website.models.product import Product
from website.models.review import Review


# definig class for Login
class ProductItem(View):
    def get(self,request):
        return redirect('home')

    def post(self,request):
        product_id = request.POST.get('product_id')
        print("Product_id: ", product_id)
        product=Product.get_product_by_exact_id(product_id)

        # fetching review form data
        review = request.POST.get('review')
        name = request.POST.get('name')
        email = request.POST.get('email')




        # storing reviews
        if review and product_id:
            reviewObject = Review(product=Product(id=product_id),
                            review = review,
                            name = name,
                            email = email)
            print(reviewObject)
            reviewObject.saveReview()






        # fetching reviews
        reviews = Review.get_review_by_product_id(product_id)
        reviews_count = 0
        if reviews:
            reviews_count = reviews.count()


        # code for adding product in the cart
        cart=request.session.get('cart')
        remove = request.POST.get('remove')
        change_in_quantity = request.POST.get('change_in_quantity')
        print("Change in Quantity: ", change_in_quantity)
        if (cart and product) and change_in_quantity:
            quantity = cart.get(product_id)
            if quantity:
                if remove:
                    if cart[product_id] <= 1:
                        cart.pop(product_id)
                    else:
                        cart[product_id] = quantity - 1
                else:
                    cart[product_id] = quantity + 1
            else:
                cart[product_id] = 1
        elif product and change_in_quantity:
            cart = {}
            cart[product_id] = 1

        if cart:
            request.session['cart'] = cart
        print("Cart : ", cart)


        data = {}
        data['product'] = product
        data['reviews'] = reviews
        data['reviews_count'] = reviews_count
        return render(request,'product.html',data)

    