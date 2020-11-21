''' Users Views. '''
# Django
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Exception
from django.db.utils import IntegrityError

# Models
from django.contrib.auth.models import User
from login.models import Profile
from dashboard.models import Card

# Forms

def index(request):
    return render(request,'index.html')

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
    return redirect('')


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
        except IntegrityError:
            return render(request, 'login/signin.html', {'error': 'Username already taken'})

        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        card = Card.objects.all()[:3]
        user.save()
        profile = profile(user = user, description = "")
        profile.save()
        for carta in card:    
            profile.cards.add(carta)
            profile.save()
        
        return redirect('login')

    return render(request,'login/signin.html')

def about_view(request):
    return render(request,'about.html')
    
def shop_view(request):
    return render(request,'shop.html')

def email_sended(request):
    print("ENTER EMAIL?SENDED")
    if request.method == 'POST':
        email = request.POST['email']
        try:
            usuario = User.objects.get(email=email)
        except User.DoesNotExist:
            return render(request,'restore/password_restore.html',{'error':'El correo no esta registrado'})
              
    return render(request,'restore/restore_done.html')

def restore_password(request):
    if request.method == 'POST':
        email = request.POST['email']
        usuario = User.objects.get(email= email)
        if usuario == undefined:
            return render(request,'restore/password_restore.html',{error:'El correo no esta registrado'})
    return render(request,'restore/password_restore.html')

def pasword_reset_confirm(request):
    """  Vista de confirmación de envio  """

    pass
def pasword_reset_done(request):
    """  Vista de confirmación de envio  """
    
    pass