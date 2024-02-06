from django.db import models
from users.models import CustomUser

""" カテゴリーモデル """
class Category(models.Model):
    name = models.CharField(verbose_name='カテゴリー', max_length=100)
    auther = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='投稿者')
    image = models.ImageField(verbose_name='画像', upload_to='category_images/', blank=True, null=True)

    def __str__(self):
        return self.name
    
""" 生産者モデル """
class Farmer(models.Model):
    farmer = models.OneToOneField(CustomUser, on_delete=models.CASCADE, verbose_name='生産者ユーザー', related_name='farmer_profile')
    farm_name = models.CharField(verbose_name='会社名 / 代表者名', max_length=50, blank=True, null=True)
    catchphrase = models.CharField(verbose_name='キャッチコピー', max_length=30, blank=True, null=True)
    comment = models.TextField(verbose_name='コメント', max_length=250, blank=True, null=True)

    def __str__(self):
        return self.farmer.username

""" レストランモデル """
class Restaurant(models.Model):
    name = models.CharField(verbose_name='店名', max_length=100)
    ruby = models.CharField(verbose_name='店名（かな）', max_length=100, blank=True, null=True)
    zip_code = models.CharField(verbose_name='郵便番号',max_length=8, blank=True)
    address1 = models.CharField(verbose_name='都道府県', max_length=40, blank=True)
    address2 = models.CharField(verbose_name='市区町村番地', max_length=40,blank=True)
    address3 = models.CharField(verbose_name='建物名', max_length=40, blank=True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='投稿者')
    messages = models.TextField(verbose_name='店長コメント', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='カテゴリー')
    image = models.ImageField(verbose_name='画像', upload_to='restaurant_images/',default='restaurant_images/no_image.png', blank=True, null=True)
    catchphrase = models.CharField(verbose_name='キャッチコピー', max_length=30, blank=True, null=True)
    comment = models.TextField(verbose_name='店舗概要', blank=True, null=True)
    recommend = models.BooleanField(verbose_name='おすすめ店舗', default=False)
    farmer_id = models.PositiveIntegerField(verbose_name='農家ID', blank=True, null=True)
    created_at = models.DateTimeField(verbose_name='作成日', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日', auto_now=True)

    def __str__(self):
        return self.name

""" レビューモデル """
SCORE_CHOICES = [
    (1, '★'),
    (2, '★★'),
    (3, '★★★'),
    (4, '★★★★'),
    (5, '★★★★★'),
]

class Review(models.Model):

    author = models.ForeignKey(CustomUser, on_delete=models.PROTECT, verbose_name='投稿者')
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, verbose_name='店名')
    score = models.PositiveSmallIntegerField(verbose_name='満足度', choices=SCORE_CHOICES, default=3, blank=False)
    title = models.CharField(verbose_name='タイトル', max_length=50, blank=False)
    comment = models.TextField(verbose_name='コメント', max_length=250, blank=False)
    created_at = models.DateTimeField(verbose_name='作成日', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日', auto_now=True)

    def __str__(self):
        return f"{self.restaurant.name} - {self.author.username}"