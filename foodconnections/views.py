from django.views import generic
from .models import Category, Restaurant

class IndexView(generic.ListView):
    model = Restaurant
    template_name = 'foodconnections/restaurant_list.html'
    context_object_name = 'restaurant_list'

class DetailView(generic.DetailView):
    model = Restaurant
    template_name = 'foodconnections/restaurant_detail.html'
    context_object_name = 'restaurant'
