from django.db import models
from users.models import CustomUser

class Category(models.Model):
    name = models.CharField(max_length=100)
    auther = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
    )

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length = 100)
    auther = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name