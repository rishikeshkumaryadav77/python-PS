from django.contrib import admin
from django.urls import path, include
from home import Views

urlpatterns = [
    path(" ", Views.index, name="home")
    path("about", Views.about, name="about")
    path("services", Views.services, name="services")
    path("contact", Views.contact, name="contact")
    
]
