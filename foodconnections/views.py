from django.views import generic
from .models import Category, Restaurant, Review
from .forms import ReviewForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.db.models import Avg
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied


class IndexView(generic.ListView):
    model = Restaurant
    template_name = 'foodconnections/restaurant_list.html'
    context_object_name = 'restaurant_list'

class DetailView(generic.DetailView):
    model = Restaurant
    template_name = 'foodconnections/restaurant_detail.html'
    context_object_name = 'restaurant'

    """ ここからレビュー表示の作成 """
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        reviews = Review.objects.filter(restaurant_id=self.kwargs['pk']) #対象店舗の全てのレビューを取得

        """レビューの平均点と総数を計算"""
        average_score_dic = reviews.aggregate(Avg('score')) #レビュースコアの平均値を算出、辞書型{'score__ave':数値}で返ってくる
        average_score = average_score_dic['score__avg']
        total_reviews = reviews.count()

        context['reviews'] = reviews
        context['average_score'] = round(average_score, 1) if average_score else 0
        context['total_reviews'] = total_reviews
        context['review_form'] = ReviewForm

        return context
    
class ReviewCreateView(generic.edit.CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'foodconnections/restaurant_detail.html'

    def form_valid(self, form):
        form.instance.user = self.request.user #投稿されたレビューにログインしているユーザーを関連付ける
        form.instance.restaurant = get_object_or_404(Restaurant, pk=self.kwargs['pk']) #投稿されたレビューに対象の店舗を関連付ける
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('foodconnections:detail', kwargs={'pk': self.kwargs.get('pk')})

class CreateView(LoginRequiredMixin, generic.edit.CreateView):
    model = Restaurant
    fields = ['name','address','category','image']
    template_name = 'foodconnections/restaurant_form.html'
    success_url = reverse_lazy('foodconnections:index')

    def form_valid(self, form):
        restaurant_name = form.cleaned_data['name']
        messages.success(self.request, f'"{restaurant_name}"を登録しました。')
        return super().form_valid(form)
    
class UpdateView(generic.edit.UpdateView):
    model = Restaurant
    fields = ['name','address','category','image']
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