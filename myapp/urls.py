from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('foodconnections/', include('foodconnections.urls')),
    path('', RedirectView.as_view(url='/foodconnections/')),
]

#開発環境での画像ファイルにアクセスするためのURLを生成
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

