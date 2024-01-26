from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone

class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        #emailがない場合のエラーメッセージ
        if not email:
            raise ValueError('メールアドレスは必須項目です。')
        email = self.normalize_email(email)
        username = self.model.normalize_username(username)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self.db)
        return user
    
    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(username, email, password, **extra_fields)
    
class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=100, blank=True)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    user_type = models.CharField(max_length=20, default='general')
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email' #認証に使うフィールドの設定
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = ['username'] #createsuperuserコマンド実行時に入力が必要なフィールド
