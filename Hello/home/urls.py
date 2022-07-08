from django.contrib import admin
from django.urls import path
from home import views

# How to change django admin panel text
admin.site.site_header = "Udoy ice-Cream Admin"
admin.site.site_title = "Udoy ice-Cream Admin Portal"
admin.site.index_title = "Welcome to Udoy ice-Creams"

# admin panel... Username >>> [ Udoy ] Password >>> [ 11223344 ]

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('services', views.services, name='services'),
    path('contact', views.contact, name='contact')
]
