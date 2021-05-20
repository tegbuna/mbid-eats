from django.shortcuts import render, get_object_or_404
from .models import Recipe
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Create your views here.

# render templates:
def index(request):
    total_recipes = Recipe.objects.all().count()
    context = {
        'title': 'Home',
        'total_recipes': total_recipes,
    }

    if request.GET:
        breakfast = request.GET.get('breakfast')
    return render(request, 'index.html', context)

def search(request):
    recipes = Recipe.objects.all()
    results = ''

    if "search" in request.GET:
        query = request.GET.get("search")
        queryset = recipes.filter(Q(title__icontains=query))

    if request.GET.get("breakfast"):
        results = queryset.filter(Q(topic__title__icontains="breakfast"))
        topic="breakfast"
    elif request.GET.get("appetizers"):
        results = queryset.filter(Q(topic__title__icontains="appetizers"))
        topic="appetizers"
    elif request.GET.get("lunch"):
        results = queryset.filter(Q(topic__title__icontains="lunch"))
        topic="lunch"
    elif request.GET.get("dinner"):
        results = queryset.filter(Q(topic__title__icontains="dinner"))
        topic="dinner"
    elif request.GET.get("soups"):
        results = queryset.filter(Q(topic__title__icontains="soups"))
        topic="soups"
    elif request.GET.get("dessert"):
        results = queryset.filter(Q(topic__title__icontains="dessert"))
        topic="dessert"

    total = results.count()

    # paginate results
    paginator = Paginator (results, 3)
    page = request.GET.get('page')
    try:
        results = paginator.page(page)
    except PageNotAnInteger:
        results = paginator.page(1)
    except EmptyPage:
        results = paginator.page(paginator.num_pages)

    context = {
        "page":page,
        "topic":topic,
        "total":total,
        "query":query,
        "results":results,

    }
    return render(request, 'search.html', context)


def details(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug)
    context = {
        'title':'Details',
        'recipe':recipe,
    }
    return render(request, 'details.html', context)
