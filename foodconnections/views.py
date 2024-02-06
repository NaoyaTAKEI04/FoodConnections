from django.views import generic, View
from .models import Category, Restaurant, Review, Farmer
from users.models import CustomUser
from .forms import ReviewForm, SearchForm, RestaurantForm, ProfileEditForm, FarmerForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.db.models import Avg, Q
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied

""" トップページの表示 """
class TopPageView(View):
    template_name = 'foodconnections/top_page.html'

    def get(self, request, *args, **kwargs):
        search_form = SearchForm()
        recommends = Restaurant.objects.filter(recommend=True)
        categories = Category.objects.all() # カテゴリ一覧を取得
        context = {
            'search_form' : search_form,
            'recommends' : recommends,
            'categories' : categories,
        }
        return render(request, self.template_name, context)

""" 検索結果の表示 """
class SearchResultsView(generic.ListView):
    model = Restaurant
    template_name = 'foodconnections/search_results.html'
    context_object_name = 'restaurant_list'

    def get_queryset(self):
        # GET パラメータから query（店名の検索キーワード）と prefecture（都道府県）を取得
        query = self.request.GET.get('query', '')
        prefecture = self.request.GET.get('prefecture', '')
        # プルダウンリストと検索フォームのいずれかに入力がある場合に検索を行う
        if query or prefecture:
            # 店名または住所のいずれかに一致するレストランを取得
            return Restaurant.objects.filter(name__icontains=query, address1__icontains=prefecture)
        else:
            return Restaurant.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search_form = SearchForm()
        context['query'] = self.request.GET.get('query', '')
        context['prefecture'] = self.request.GET.get('prefecture', '')
        context['search_form'] = search_form
        return context

""" 該当カテゴリーの飲食店一覧を表示 """
class CategoryListView(View):
    template_name = 'foodconnections/category_list.html'

    def get(self, request, category_id, *args, **kwargs):
        category = get_object_or_404(Category, id=category_id) #該当するカテゴリを代入
        restaurants = Restaurant.objects.filter(category=category) # カテゴリに属する飲食店一覧を取得
        context = {
            'category':category,
            'restaurants':restaurants,
        }
        return render(request, self.template_name, context)

""" マイページの表示 """
class MyPageView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'foodconnections/my_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user # アクセスユーザーの情報を取得
        user_restaurants = Restaurant.objects.filter(author=user) # アクセスユーザーが投稿者に該当する飲食店の情報を取得
        user_reviews = Review.objects.filter(author=user) # アクセスユーザーが投稿者に該当するレビューの情報を取得
        user_farm = Farmer.objects.filter(farmer=user) # アクセスユーザーが投稿者に該当する生産者情報を取得
        context['user_info'] = user
        context['user_restaurants'] = user_restaurants
        context['user_reviews'] = user_reviews
        context['user_farm'] = user_farm
        return context
    
""" マイページの編集 """
class ProfileEditView(LoginRequiredMixin, generic.UpdateView):
    model = CustomUser
    form_class = ProfileEditForm
    template_name = 'foodconnections/profile_edit.html'
    success_url = reverse_lazy('foodconnections:my_page')

    def get_object(self, queryset=None):
        return self.request.user  # ログイン中のユーザーを取得

    def form_valid(self, form):
        messages.success(self.request, 'プロフィールが更新されました。')
        return super().form_valid(form)

""" 飲食店の詳細ページの表示 """
class DetailView(generic.DetailView):
    model = Restaurant
    template_name = 'foodconnections/restaurant_detail.html'
    context_object_name = 'restaurant'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        reviews = Review.objects.filter(restaurant_id=self.kwargs['pk']) # 対象飲食店の全てのレビューを取得

        """レビューの平均点と総数を計算"""
        average_score_dic = reviews.aggregate(Avg('score')) # レビュースコアの平均値を算出、辞書型{'score__ave':数値}で返ってくる
        average_score = average_score_dic['score__avg']
        total_reviews = reviews.count()

        context['reviews'] = reviews
        context['average_score'] = round(average_score, 1) if average_score else 0
        context['total_reviews'] = total_reviews

        context['review_form'] = ReviewForm # ReviewFormのインスタンスを作成し、コンテキストに追加

        """生産者の情報を取得"""
        # 飲食店が紐づけた農家の ID を取得
        farmer_id = self.object.farmer_id

        # 生産者の情報を取得
        if farmer_id:
            farmer = get_object_or_404(Farmer, pk=farmer_id)
            farmer_data = {
                'farmer_name' : farmer.farmer.username,
                'profile_image' : farmer.farmer.profile_image,
                'farm_name' : farmer.farm_name,
                'catchphrase' : farmer.catchphrase,
                'comment' : farmer.comment,
            }
        else:
            farmer_data = None

        context['farmer_data'] = farmer_data

        return context
    
""" レビューの作成 """
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

""" 飲食店の詳細ページの作成 """
class CreateView(LoginRequiredMixin, generic.edit.CreateView):
    model = Restaurant
    form_class = RestaurantForm
    template_name = 'foodconnections/restaurant_form.html'
    success_url = reverse_lazy('foodconnections:top_page')

    def form_valid(self, form):
        form.instance.author = self.request.user # ログインしているユーザー名を投稿者にする
        restaurant_name = form.cleaned_data['name'] # フォームに入力された店名を代入
        messages.success(self.request, f'"{restaurant_name}"を登録しました。') # 新規作成完了時のメッセージ
        return super(CreateView, self).form_valid(form)

""" 飲食店の詳細ページの編集 """
class UpdateView(generic.edit.UpdateView):
    model = Restaurant
    form_class = RestaurantForm
    template_name = 'foodconnections/restaurant_form.html'
    context_object_name = 'restaurant'

    def form_valid(self, form):
        messages.success(self.request, 'お店の情報が編集されました。')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('foodconnections:detail', kwargs={'pk':self.object.pk})

""" 飲食店の詳細ページの削除 """
class DeleteView(generic.DeleteView):
    model = Restaurant
    template_name = 'foodconnections/restaurant_comfirm_delete.html'
    context_object_name = 'restaurant'
    success_url = reverse_lazy('foodconnections:top_page')

    def delete(self, request, *args, **kwargs):
        delete_instance = self.get_object()
        shop_name = delete_instance.name
        messages.success(self.request, f'"{ shop_name }"を削除しました。')
        return super().delete(request, *args, **kwargs)

""" レビューの削除 """  
class ReviewDeleteView(generic.DeleteView):
    model = Review
    template_name = 'foodconnections/review_comfirm_delete.html'
    context_object_name = 'review'
    success_url = reverse_lazy('foodconnections:my_page')

    def delete(self, request, *args, **kwargs):
        delete_instance = self.get_object()
        messages.success(self.request, 'レビューを削除しました。')
        return super().delete(request, *args, **kwargs)
    
""" 生産者情報の編集 """    
class FarmerEditView(LoginRequiredMixin, generic.edit.UpdateView):
    model = Farmer
    form_class = FarmerForm
    template_name = 'foodconnections/farmer_edit.html'
    success_url = reverse_lazy('foodconnections:my_page')
    context_object_name = 'farmer'

    def get_object(self, queryset=None):
        if not hasattr(self.request.user, 'farmer_profile'): # ユーザーが Farmer プロフィールを持っていない場合は作成する
            Farmer.objects.create(farmer=self.request.user)
        return self.request.user.farmer_profile  # ログイン中のユーザーの Farmer プロフィールを取得

    def form_valid(self, form):
        messages.success(self.request, '生産者情報が更新されました。')
        return super().form_valid(form)