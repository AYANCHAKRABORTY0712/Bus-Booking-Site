from django.shortcuts import HttpResponse,render, redirect
from datetime import datetime
from booking.models import USER,BUS,Booking,Contact
from django.db import IntegrityError
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from booking.func import CreateBus
import random


#user options context

def context(request):
    if request.user.is_authenticated:
        context={
            "auth": 1,
            "username": request.user.username,
            "mail_id": request.user.email
        }
        return context

def index(request):
    return render(request, 'index.html',context(request))

def register(request):
    if request.method == "POST":
        name = request.POST.get('name')
        age = request.POST.get('age')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        email = request.POST.get('mail id')
        username = request.POST.get('username')
        password = request.POST.get('password')
        date = datetime.today()
        user = USER(name=name, age=age, phone=phone, address=address, email=email, username=username, password=password, date=date)
        user.save()
        try:
            user = User.objects.create_user(
            username = username,
            password = password,
            email = email
            )

            return render(request, 'successfully_registered.html')

        except IntegrityError:

            messages.error(request, 'This username already exists!')
            return redirect('/register/')
        
        
    return render(request, 'register.html')

def homepage(request):
    if request.user.is_authenticated:
        contxt=context(request)
        if request.method == "POST":
            From = request.POST.get('from')
            To = request.POST.get('to')
            Date = request.POST.get('date')
            
            buses=BUS.objects.filter(From=From,To=To,Date=Date)

            #return HttpResponse(str(buses.count()))

            if(buses.count()<6):
                init_count=buses.count()
                final_count=random.randint(7,12)
                
                while(init_count<final_count):
                    CreateBus(From,To,Date)
                    init_count+=1

            contxt.update({'buses':buses})

        return render(request, 'homepage.html', contxt)
    else:
        return redirect('/login/')
    

def booking(request):
    if request.user.is_authenticated:
        return render(request, 'booking.html', context(request))
    else:
        return redirect('/login/')

def Login(request):
    if request.method=="POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        
        else:
            return redirect('/login/')
        
    return render(request, 'login.html')

            

def Logout(request):
    logout(request)
    return redirect('/')
    
def checkout(request):
    if request.user.is_authenticated:
        return render(request, 'payment.html', context(request))
    else:
        return redirect('/login/')

def selection(request):
    if request.user.is_authenticated:
        return render(request, 'selection.html', context(request))
    else:
        return redirect('/login/')

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')