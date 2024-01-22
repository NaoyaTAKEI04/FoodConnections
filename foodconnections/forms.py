from django import forms
from django.forms import ModelForm
from .models import Restaurant, Review

class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ['name', 'ruby', 'zip_code', 'address1', 'address2', 'address3', 'category', 'image', 'catchphrase', 'comment']

        widgets = {
            'zip_code':
            forms.TextInput(
                #attrsでp-postal-codeを指定
                attrs={'class': 'p-postal-code', 'placeholder': '記入例：8900053',}, 
            ),
            'address1': forms.TextInput(
                #attrsでp-regionを指定
                attrs={'class': 'p-region', 'placeholder': '記入例：鹿児島県'}, 
            ),
            'address2': forms.TextInput(
                #attrsでp-locality p-street-address p-extended-addressを指定
                attrs={'class': 'p-locality p-street-address p-extended-address', 'placeholder': '記入例：鹿児島市中央町10'}, 
            ),
            'address3': forms.TextInput(
                attrs={'class': '','placeholder': '記入例：キャンセビル'}, 
            ),
        }

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