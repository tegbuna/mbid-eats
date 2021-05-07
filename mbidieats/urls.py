# import path:
from django.urls import path

# import views (like express controllers):
from . import views

# list all individual url pattern paths:
urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
    path('details/', views.details, name='details'),
]




