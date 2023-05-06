from django.urls import path
from . import views

urlpatterns = [
    path('home', views.landing, name = 'home'),
    path('register', views.register, name = 'register'),
    path('login', views.loginpage, name = 'login'),
    path('logout', views.logoutpage, name = 'logout'),
    path('restriction', views.restriction, name = 'restriction'),
    path('about', views.about, name = 'about'),
]