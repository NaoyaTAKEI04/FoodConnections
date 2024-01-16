from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):   
    class Meta:
        model = Review
        fields = ['score', 'title', 'comment']

class SearchForm(forms.Form):
    query = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={'placeholder': '店名または住所から探す'}), # 検索フォームに初期値を設定
        max_length=100,
    )