
from django.urls import path
from .import views
from .views import DonateFoodView,DonationHistoryView,FeedbackView,FeedbacklistView,DonationEditView,DonationDeleteView,RequestListView


urlpatterns = [
    path('index',views.home,name="index"),
    path('donate-food',DonateFoodView.as_view(),name='donate-food'),
    path('donation-history',DonationHistoryView.as_view(),name='donation-history'),
    path('feedback',FeedbackView.as_view(),name="feedback"),
    path('feedback-list',FeedbacklistView.as_view(),name="feedback-list"),
    path('donation-edit/<int:pk>',DonationEditView.as_view(),name="donation-edit"),
    path('donation-delete/<int:pk>',DonationDeleteView.as_view(),name='donation-delete'),
    path('request-view',RequestListView.as_view(),name='requestview')

]
