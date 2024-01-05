from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.views import generic
from .models import Category, Restaurant
from django.urls import reverse_lazy
from django.contrib import messages

class IndexView(generic.ListView):
    model = Restaurant
    template_name = 'foodconnections/restaurant_list.html'
    context_object_name = 'restaurant_list'

class DetailView(generic.DetailView):
    model = Restaurant
    template_name = 'foodconnections/restaurant_detail.html'
    context_object_name = 'restaurant'

class CreateView(generic.edit.CreateView):
    model = Restaurant
    fields ='__all__'
    template_name = 'foodconnections/restaurant_form.html'
    success_url = reverse_lazy('foodconnections:index')

    def form_valid(self, form):
        restaurant_name = form.cleaned_data['name']
        messages.success(self.request, f'"{restaurant_name}"を登録しました。')
        return super().form_valid(form)
