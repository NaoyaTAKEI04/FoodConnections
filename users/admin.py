from django.contrib import admin
from .models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
    # 一覧画面: 表示項目
    list_display = (
        "email",
        "username",
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

    # 詳細画面: 表示項目
    basic = ("username", "email", "password")
    personal = ("last_name", "first_name", "date_joined")
    auth = ("is_staff", "is_active")

    fieldsets = (
        ("BasicInfo", {"fields": basic}),
        ("Personal", {"fields": personal}),
        ("Auth", {"fields": auth}),
    )

admin.site.register(CustomUser, CustomUserAdmin)