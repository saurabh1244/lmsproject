
from django.urls import path , include
from .views import *


urlpatterns = [
    path("",home,name="home"),
    path("register/",register_page,name="register_page"),
    path("verify-email/<slug:username>/",verify_email,name="verify-email"),
    path("resend-otp/",resend_otp,name="resend-otp"),
    path("login",login_page,name="login_page"),
    path('update_password/',update_password,name="update_password"),
    path('profile_update/',profile_update,name="profile_update"), 
    path('logout_user/',logout_user,name="logout_user"),   
    path('forget_pass/',forget_pass,name="forget_pass"),   
    path('purchased/',purchased,name="purchased"),
    path('product/<int:id>',product,name="product"),
    path('purchasedx/',purchasedx,name="purchasedx"),
    path('category/<str:name>/',category,name="category"),
    path('search/',search,name="search"),




    

]
