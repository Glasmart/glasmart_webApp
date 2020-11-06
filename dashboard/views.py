from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Models
from login.models import User
from dashboard.models import Card
# Create your views here.

@login_required
def home(request):
    _user = User.objects.get(id=request.user.id)
    user_cards= _user.profile.cards.all()
    
    return render(request,'dashboard/index.html',{'userCards':user_cards})

@login_required
def turn_card(request):
    
    return render(request,'dashboard/index.html')
    

@login_required
def create_first_cards(request):
    # UP = UserProfile.objects.get(id = request.POST['profile'])
    # if UP.id_profile.name == "Administrador":
    #     for card in Card.objects.all() :
    #         UserCard(id_user=request.user, id_profile=UP.id_profile, id_card=card).save()
    # if UP.id_profile.name == "Basico":
    #     for card in Card.objects.all()[:2] :
    #         UserCard(id_user=request.user, id_profile=UP.id_profile, id_card=card).save()
    # if UP.id_profile.name == "Moderado":
    #     for card in Card.objects.all()[:4] :
    #         UserCard(id_user=request.user, id_profile=UP.id_profile, id_card=card).save()

    return render(request,'dashboard/index.html')


