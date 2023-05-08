
from django.urls import path
from .import views



urlpatterns = [
    path('index',views.home,name="index"),
    path('donate_food',views.donate_food,name='donate-food'),
    path('donation_history',views.donation_history,name='donation-history'),


    
]
