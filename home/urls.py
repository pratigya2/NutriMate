from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name = 'home'),
    path('register', views.register, name = 'register'),
    path('login', views.loginpage, name = 'login'),
    path('logout', views.logoutpage, name = 'logout'),
    path('restriction', views.restriction, name = 'restriction'),
    path('about', views.about, name = 'about'),
    path('index', views.index, name = 'index'),
    path('detail/<slug:slug>', views.detail, name = 'detail'),
]
