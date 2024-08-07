from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage),
    path('burger', views.burgerpage),
    path('biryani', views.biryanipage),
    path('cake', views.cakepage),
    path('drink', views.drinkpage),
    path('icecream', views.icecreampage),
    path('momos', views.momospage),
    path('noodles', views.noodlespage),
    path('northfood', views.northfoodpage),
    path('pizza', views.pizzapage),
    path('southfood', views.southfoodpage),
    path('signup', views.signuppage),
    path('login', views.loginpage),
    path('product/<int:Id>', views.productpage),
    path('products/<int:Id>', views.productpagess),
    path('addcart/<int:ID>/', views.addToCart),
    path('addcarts/<int:ID>/', views.addToCarts),
    path('cart', views.cartpage),
    path('logout',views.logout),
    path('search/<str:item>',views.searchpage),

]
