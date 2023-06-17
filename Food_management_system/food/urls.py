from django.urls import path
from food import views

from . import views

app_name = 'food'

urlpatterns = [
    path('index1',views.index1,name="index1"),
    
    path('d_view_profile/',views.d_view_profile,name='d_view_profile'),
    path('d_edit_profile/', views.d_edit_profile, name='d_edit_profile'),
    
    path('request_donation',views.request_donation,name='request-donation'),
    path('vfdetails/', views.vfdetails, name="vfdetails"),
    path('vohistory', views.vohistory, name="vohistory"),
    path('pmanagement', views.pmanagement, name="pmanagement"),
    path('order/', views.order, name="order"),
    path('viewreq', views.viewreq, name="viewreq"),
    path('fddetails', views.fddetails, name="fddetails"),
    path('ohistory', views.ohistory, name="ohistory"),
    path('confirmation', views.confirmation, name="confirmation"),

]