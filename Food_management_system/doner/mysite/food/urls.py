from django.urls import path

from . import views

app_name = 'food'

urlpatterns = [
    path('vfdetails', views.vfdetails, name="vfdetails"),
    path('vohistory', views.vohistory, name="vohistory"),
    path('pmanagement', views.pmanagement, name="pmanagement"),
    path('uploadf', views.uploadf, name="uploadf"),
    path('updatef', views.updatef, name="updatef"),
    path('fddetails', views.fddetails, name="fddetails"),
    path('ohistory', views.ohistory, name="ohistory"),
    path('confirmation', views.confirmation, name="confirmation"),

]