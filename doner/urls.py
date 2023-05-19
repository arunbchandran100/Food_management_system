
from django.urls import path
from .import views
from .views import DonateFoodView,DonationHistoryView


urlpatterns = [
    path('index',views.home,name="index"),
    path('donate_food',DonateFoodView.as_view(),name='donate-food'),
    path('donation_history',DonationHistoryView.as_view(),name='donation-history')

    

    
]
