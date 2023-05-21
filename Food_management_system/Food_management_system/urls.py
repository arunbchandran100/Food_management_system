
from django.contrib import admin
from django.urls import path,include
from website import views
#from .views import UserEditView
from django.contrib.auth import views as auth_views 
import doner

urlpatterns = [
    path('admin/', admin.site.urls),
    path('website/', include('website.urls')),
    path('doner/',include('doner.urls')),
    path('distributor/',include('distributor.urls')),

]