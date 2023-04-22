
from django.contrib import admin
from django.urls import path
from website import views
#from .views import UserEditView
from django.contrib.auth import views as auth_views 
import doner


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.SignupPage,name='signup'),
    path('login/',views.LoginPage,name='login'),
    path('home/',views.HomePage,name='home'),
    path('logout/',views.LogoutPage,name='logout'),
    
    path('vprofile/',views.profile,name='vprofile'),
    
    path('forget_password/' ,views.ForgetPassword , name="forget_password"),
    path('change_password/<token>/' , views.ChangePassword , name="change_password"),
    #path('admin/', admin.site.urls),
    path('website/', include('website.urls')),
    path('doner/',include('doner.urls')),
]
