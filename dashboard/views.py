from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Models
from login.models import UserProfile, Profile
from dashboard.models import UserCard,Card
# Create your views here.

@login_required
def home(request):
    user = request.user
    uprofile = UserProfile.objects.get(id_user=user)
    print(uprofile)
    usercards = UserCard.objects.filter(id_user=user)
    print(usercards)
    return render(request,'dashboard/index.html',{'userCards':usercards,'uprofile':uprofile})

@login_required
def turn_card(request):
    card = UserCard.objects.get(id=request.card)
    card.toggleActive()
    return render(request,'dashboard/index.html')

@login_required
def create_first_cards(request):
    
    UP = UserProfile.objects.get(id = request.POST['profile'])
    if UP.id_profile.name == "Administrador":
        for card in Card.objects.all() :
            UserCard(id_user=request.user, id_profile=UP.id_profile).save()
    if UP.id_profile.name == "Basico":
        for card in Card.objects.all()[:2] :
            UserCard(id_user=request.user, id_profile=UP.id_profile).save()
    if UP.id_profile.name == "Moderado":
        for card in Card.objects.all()[:4] :
            UserCard(id_user=request.user, id_profile=UP.id_profile).save()
    return render(request,'dashboard/index.html')