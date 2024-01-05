from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('foodconnections/', include('foodconnections.urls')),
    path('', RedirectView.as_view(url='/foodconnections/')),
]
