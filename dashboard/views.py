from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Models
from login.models import Profile
from dashboard.models import Card
# Create your views here.

@login_required
def home(request):
    user = request.user
    # uprofile = UserProfile.objects.get(id_user=user)
    # print(uprofile)
    # usercards = UserCard.objects.filter(id_user=user)
    # print(usercards)
    # return render(request,'dashboard/index.html',{'userCards':usercards,'uprofile':uprofile})

@login_required
def turn_card(request):

    pass
    

@login_required
def create_first_cards(request):
    pass
    


