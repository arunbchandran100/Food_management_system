
from django.contrib import admin
from django.urls import path,include
from website import views
#from .views import UserEditView
from django.contrib.auth import views as auth_views 


urlpatterns = [
    path('',views.basehome,name='bhome'),#homepage before login
    path('signup',views.SignupPage,name='signup'),
    path('login/',views.LoginPage,name='login'),
    path('home/',views.HomePage,name='home'),
    path('logout/',views.LogoutPage,name='logout'),
    
    path('vprofile/',views.profile,name='vprofile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    
    path('forget_password/' ,views.ForgetPassword , name="forget_password"),
    path('change_password/<token>/' , views.ChangePassword , name="change_password"),
]