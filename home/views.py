from django.shortcuts import render,redirect, HttpResponseRedirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .qr import generate
from .recommend import *
import json
import re

global Meal
def landing(request):
    context = Ingredients.objects.all()
    return render(request,'carousel.html',{'context':context})

def register(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        if pass1 != pass2:
            return HttpResponse("Your password and confirm password are not same")
        else:
            my_user = User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
    return render(request,'register.html')

def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('pass')
        user = authenticate(request,username=username,password = password)
        if user is not None:
            login(request,user)
            return redirect('about')
        else:
            return HttpResponse("incorrect")
    return render(request,'login.html')

def logoutpage(request):
    logout(request)
    return redirect('login')
def about(request):
    return render(request,'carousel.html')
def restriction(request):
    if request.method == 'POST':
        gluton = request.POST.get('gluten')
        sugar = request.POST.get('sugar')
        keto= request.POST.get('keto')
        veg = request.POST.get('veg')
        dairy = request.POST.get('dairy')
        paleo = request.POST.get('paleo')
        oily = request.POST.get('oily')
        if not veg:
            veg = 0.5
        if not dairy:
            dairy = 0.5
        if not oily:
            oily = 0.5
        Input = [gluton,sugar,keto,veg,dairy,paleo,oily]
        Meal = implementation(Input)
        request.session['meals'] = Meal
        return HttpResponseRedirect('index')
        
    return render(request,'restriction.html')
def index(request):
    data = request.session.get('meals')
    meals = []
    for meal in data:
        meals.append(list(Ingredients.objects.filter(name = meal).values()))

    print(meals)

    return render(request,'index.html',{'meals':meals})

def detail(request,slug):
    item = Ingredients.objects.filter(id = slug)
    name = Ingredients.objects.values('name').get(id=slug)['name']
    print(name)
    link = Ingredients.objects.values('meal_link').get(id=slug)['meal_link']
    path = name+".png"
    new = generate(name,link,path)
    print(new)
    return render(request,'detail.html',{'item': item})
# Create your views here.