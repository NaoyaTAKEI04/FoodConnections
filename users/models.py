from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone
from allauth.account.models import EmailAddress

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
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)

    USER_TYPE_CHOICES = (
        ('general', '一般ユーザー'),
        ('restaurant_owner', '飲食店オーナー'),
        ('farmer', '農家'),
    )
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES, default='general')

    objects = CustomUserManager()

    USERNAME_FIELD = 'email' #認証に使うフィールドの設定
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = ['username'] #createsuperuserコマンド実行時に入力が必要なフィールド

    def verified_email(self): #メール認証が済んでいるかどうかを管理画面に表示
        return EmailAddress.objects.filter(user=self, verified=True).exists()

    verified_email.boolean = True  # 表示をTrue/Falseに変更
    verified_email.short_description = 'Verified Email'  # 列ヘッダーの表示

    def __str__(self):
        return self.username
