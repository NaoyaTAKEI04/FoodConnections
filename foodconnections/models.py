from django.db import models
from users.models import CustomUser

class Category(models.Model):
    name = models.CharField(verbose_name='カテゴリー', max_length=100)
    auther = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
    )
    image = models.ImageField(verbose_name='画像', upload_to='category_images/', blank=True, null=True)

    def __str__(self):
        return self.name

class Restaurant(models.Model):
    name = models.CharField(verbose_name='店名', max_length=100)
    address = models.CharField(verbose_name='住所', max_length = 100)
    author = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        verbose_name='カテゴリー',
    )
    image = models.ImageField(verbose_name='画像', upload_to='restaurant_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

""" レビューのモデル """
SCORE_CHOICES = [
    (1, '★'),
    (2, '★★'),
    (3, '★★★'),
    (4, '★★★★'),
    (5, '★★★★★'),
]

class Review(models.Model):

    user = models.ForeignKey(CustomUser, on_delete=models.PROTECT)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    score = models.PositiveSmallIntegerField(verbose_name='満足度', choices=SCORE_CHOICES, default=3, blank=False)
    title = models.CharField(verbose_name='タイトル', max_length=50, blank=False)
    comment = models.TextField(verbose_name='コメント', max_length=250, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.restaurant.name} - {self.user.username}"