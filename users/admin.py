from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    # 管理者ページの一覧表示で表示されるフィールドを指定
    list_display = (
        "id",
        "email",
        "username",
        "verified_email",
        "is_staff",
        "is_active",
        "date_joined",
    )
    # 一覧画面: サイドバーフィルター
    list_filter = (
        "email",
        "is_staff",
        "is_active",
    )

    # 一覧画面: 検索ボックス
    search_fields = ("email",)

    # 一覧画面: ソート（降順ならフィールド名の先頭に-）
    ordering = ("email",)

    # ユーザーの編集画面でのフォームのセクションとその中で表示されるフィールドを指定
    fieldsets = (
        ("BasicInfo", {"fields": ("username", "email", "password",)}),
        ("Personal", {"fields": ("date_joined", "user_type", "profile_image",)}),
        ("Auth", {"fields": ("is_staff", "is_active",)}),
    )

admin.site.register(CustomUser, CustomUserAdmin)