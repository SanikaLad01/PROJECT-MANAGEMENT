from .import views
from django.urls import path

urlpatterns = [
    
    path ('', views.home),
    path('contactus/',views.contactUs),
    path('contactsubmit/',views.contactSubmit),
]