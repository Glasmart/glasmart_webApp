from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'dashboard/index.html')

def turn_card(request):
    return render(request,'dashboard/index.html')