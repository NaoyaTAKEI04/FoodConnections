from django.forms.models import BaseModelForm
from django.http import HttpRequest, HttpResponse
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
    
class UpdateView(generic.edit.UpdateView):
    model = Restaurant
    fields = '__all__'
    template_name = 'foodconnections/restaurant_form.html'
    context_object_name = 'restaurant'

    def form_valid(self, form):
        messages.success(self.request, '編集内容が反映されました。')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('foodconnections:detail', kwargs={'pk':self.object.pk})

class DeleteView(generic.DeleteView):
    model = Restaurant
    template_name = 'foodconnections/restaurant_comfirm_delete.html'
    context_object_name = 'restaurant'
    success_url = reverse_lazy('foodconnections:index')

    def delete(self, request, *args, **kwargs):
        delete_instance = self.get_object()
        shop_name = delete_instance.name
        messages.success(self.request, f'"{ shop_name }"を削除しました。')
        return super().delete(request, *args, **kwargs)