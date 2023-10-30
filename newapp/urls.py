from django.urls import path
from . import views

urlpatterns = [
    path('login',views.index, name = 'index'),
    path('home',views.home, name = 'home'),
    path('signup',views.signup, name = 'signup'),
    path('contact',views.contact, name = 'contact'),
    path('news',views.news, name= 'news'),
]