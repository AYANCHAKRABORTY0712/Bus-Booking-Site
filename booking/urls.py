from django.contrib import admin
from django.urls import path,include
from booking import views

urlpatterns = [
    path('',views.index,name='index'),
    path('register/',views.register,name='registration'),
    path('homepage/',views.homepage,name='home'),
    path('booking/',views.booking,name='booking'),
    path('login/',views.Login,name='login'),
    path('logout/',views.Logout,name='logout'),
    path('checkout/',views.checkout,name='checkout'),
    path('selection/',views.selection,name='selection'),
    path('contact/',views.contact,name='contact'),
    path('about/',views.about,name='about')
]
