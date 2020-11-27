from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Models
from login.models import User, Products
from dashboard.models import Card
# Create your views here.

@login_required
def home(request):
    _user = User.objects.get(id=request.user.id)
    user_cards= _user.profile.cards.all()
    if _user.profile.type_user == "admin":
        _cards = Card.objects.all()
        pass
    if _user.profile.type_user == "basic":
        _cards = Card.objects.all()[:3]
        pass
    if _user.profile.type_user == "medium":
        _cards = Card.objects.all()[:5]
        pass
    
    return render(request,
        'dashboard/dashboard.html',
        {
            'userCards':user_cards,
            'cards':_cards,
        }
    )

@login_required
def turn_card(request):
    if request.method == 'POST':
        print(request.POST)
        id_card = request.POST.id
        card = Card.objects.get(id=id_card) 
        card.toggleActivo() 
        return redirect ('/dashboard/home/')
    return redirect ('/dashboard/home/')
    

@login_required
def shop(request):
    productos = Products.objects.all()
    return render(request, 'dashboard/shop.html',{'productos':productos})

@login_required
def create_first_cards(request):
    if request.method == 'POST':
        print(request.user.profile.type_user)
        if request.user.profile.type_user == "basic":
            print(request.user.profile.cards.all())
            _profile = request.user.profile
            cards = Card.objects.all()[:3]
            for _card in cards:
                _profile.cards.add(_card)
                pass
            pass
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

        return redirect ('/dashboard/home/')
    return redirect ('/dashboard/home/')


