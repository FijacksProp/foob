from django.shortcuts import render
from .models import Menu

# Create your views here.
def home(request):

    return render(request, 'food/landing_food.html')

def menu_list(request):
    menu = Menu.objects.all()
    return render(request, 'food/FoodRecipe.html', {'menu': menu})

def signup(request):

    return render(request, 'food/signup.html')