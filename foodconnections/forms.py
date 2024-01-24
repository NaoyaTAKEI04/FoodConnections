from django import forms
from django.forms import ModelForm
from .models import Restaurant, Review
from users.models import CustomUser

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
        widget=forms.TextInput(attrs={'placeholder': '店名から探す'}), # 検索フォームに初期値を設定
        max_length=100,
        required=False,
    )

    prefecture = forms.CharField(
        label='',
        widget=forms.Select(choices=[('', 'エリアから探す'),
        ('北海道', '北海道'), ('青森県', '青森県'), ('岩手県', '岩手県'), ('宮城県', '宮城県'),
        ('秋田県', '秋田県'), ('山形県', '山形県'), ('福島県', '福島県'), ('茨城県', '茨城県'),
        ('栃木県', '栃木県'), ('群馬県', '群馬県'), ('埼玉県', '埼玉県'), ('千葉県', '千葉県'),
        ('東京都', '東京都'), ('神奈川県', '神奈川県'), ('新潟県', '新潟県'), ('富山県', '富山県'),
        ('石川県', '石川県'), ('福井県', '福井県'), ('山梨県', '山梨県'), ('長野県', '長野県'),
        ('岐阜県', '岐阜県'), ('静岡県', '静岡県'), ('愛知県', '愛知県'), ('三重県', '三重県'),
        ('滋賀県', '滋賀県'), ('京都府', '京都府'), ('大阪府', '大阪府'), ('兵庫県', '兵庫県'),
        ('奈良県', '奈良県'), ('和歌山県', '和歌山県'), ('鳥取県', '鳥取県'), ('島根県', '島根県'),
        ('岡山県', '岡山県'), ('広島県', '広島県'), ('山口県', '山口県'), ('徳島県', '徳島県'),
        ('香川県', '香川県'), ('愛媛県', '愛媛県'), ('高知県', '高知県'), ('福岡県', '福岡県'),
        ('佐賀県', '佐賀県'), ('長崎県', '長崎県'), ('熊本県', '熊本県'), ('大分県', '大分県'),
        ('宮崎県', '宮崎県'), ('鹿児島県', '鹿児島県'), ('沖縄県', '沖縄県'),]),
        required=False,
    )

""" マイページの編集フォーム """
class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'profile_image']