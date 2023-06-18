from django.urls import path
from food import views

from . import views
from .views import RequestDonationView,RequestEditView,RequestDeleteView

app_name = 'food'

urlpatterns = [
    path('index1',views.index1,name="index1"),
    path('request_donation',RequestDonationView.as_view(),name='request-donation'),
    path('vfdetails/', views.vfdetails, name="vfdetails"),
    path('vohistory', views.vohistory, name="vohistory"),
    path('pmanagement', views.pmanagement, name="pmanagement"),
    path('order/<int:donation_id>/', views.order, name='order'),
    path('viewreq', views.viewreq, name="viewreq"),
    path('fddetails', views.fddetails, name="fddetails"),
    path('ohistory', views.ohistory, name="ohistory"),
    path('confirmation', views.confirmation, name="confirmation"),
    path('request-edit/<int:pk>',RequestEditView.as_view(),name="request-edit"),
    path('request-delete/<int:pk>',RequestDeleteView.as_view(),name='request-delete'),
    
    
    path('d_view_profile/',views.d_view_profile,name='d_view_profile'),
    path('d_edit_profile/', views.d_edit_profile, name='d_edit_profile'),

]