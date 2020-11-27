''' Users Views. '''
# Django
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import datetime
# Exception
from django.db.utils import IntegrityError

# Models
from django.contrib.auth.models import User
from login.models import Profile, Products
from dashboard.models import Card

# Forms
from django import forms

def index(request):
    return render(request,'home.html')

def login_view(request):
    ''' Login view '''

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['passwd']

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect ('/dashboard/home/')
        else:
            return render(request,'login/login.html',{'error':'Invalid username and password'})

    return render(request, 'login/login.html')


@login_required
def logout_view(request):
    """ Logout a user """
    logout(request)
    return render(request, 'login/login.html')


def signin(request):
    """ Sign up view """
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['passwd']
        password_confirmation = request.POST['passwd_confirmation']

        if password != password_confirmation:
            return render(request, 'login/signin.html', {'error': 'Password do not match'})

        try:
            user = User.objects.create_user(username=username, password=password)
            user.first_name = request.POST['first_name']
            user.last_name = request.POST['last_name']
            user.email = request.POST['email']
            user.save()
        except IntegrityError:
            return render(request, 'login/signin.html', {'error': 'Username already taken'})

        try:
            profile = Profile(user= user, type_user='basic',birthdate=request.POST['birthdate'])
            card = Card.objects.all()[:3]
            profile.save()
            for carta in card:    
                profile.cards.add(carta)
                profile.save()
        except IntegrityError:
            render(request, 'login/signin.html', {'error': 'Username already taken'})
        
        return redirect('login')
        
    x = datetime.datetime.now()
    today = x.strftime("%Y")+"-"+x.strftime("%m")+"-"+x.strftime("%d")
    return render(request,'login/signin.html',{'today':today})

def about_view(request):
    return render(request,'about.html')
    
def shop_view(request):
    productos = Products.objects.all()
    return render(request,'shop.html',{'productos':productos})

