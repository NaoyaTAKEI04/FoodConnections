from django.urls import path
from . import views

app_name = 'foodconnections'

urlpatterns = [
    path('', views.TopPageView.as_view(), name='top_page'),
    path('<int:category_id>/category/', views.CategoryListView.as_view(), name='category_list'),
    path('<int:pk>/detail/', views.DetailView.as_view(), name='detail'),
    path('create/', views.CreateView.as_view(), name='create'),
    path('<int:pk>/update/', views.UpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', views.DeleteView.as_view(), name='delete'),
    path('<int:pk>/review_create/', views.ReviewCreateView.as_view(), name='review_create'),
    path('<int:pk>/review_delete/', views.ReviewDeleteView.as_view(), name='review_delete'),
    path('search/', views.SearchResultsView.as_view(), name='search_results'),
    path('my_page/', views.MyPageView.as_view(), name='my_page'),
]