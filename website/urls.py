from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views
from .views.shop import Shop
from .views.login import Login
from .views.signup import SignUp
from .views.cart import Cart
from .views.product import ProductItem
from .views.checkout import CheckOut
from .views.order import OrderView
from .views.contact import Contact
from .views.home import logout, home, about, blog, elements, portfolio_item, blog_single, shop_single, portfolio_category
from .middlewares.auth import auth_middleware

urlpatterns = [
    path('', home, name='home'),
    path('logout',logout,name='logout'),
    path('contact.html',Contact.as_view(), name='contact'),
    path('orders.html',auth_middleware(OrderView.as_view()),name='orders'),
    path('checkout',CheckOut.as_view(),name='checkout'),
    path('cart.html',Cart.as_view(),name='cart'),
    path('signup.html',SignUp.as_view(),name='signup'),
    path('product',ProductItem.as_view(),name='product'),
    path('shop.html',Shop.as_view(),name='shop'),
    path('login.html',Login.as_view(),name='login'),
    path('about.html',about,name='about'),
    path('shop-single.html',shop_single,name='shop_single'),
    path('product-category.html',portfolio_category,name='portfolio_category'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)