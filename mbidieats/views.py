from django.shortcuts import render
from .models import Recipe

# Create your views here.

# render templates:
def index(request):
    total_recipes = Recipe.objects.all().count()
    context = {
        'title': 'Home',
        'total_recipes': total_recipes,
    }
    return render(request, 'index.html', context)

def search(request):
    context = {
        'title': 'Search',
    }
    return render(request, 'search.html', context)

def details(request):
    context = {
        'title': 'Details',
    }
    return render(request, 'details.html', context)
