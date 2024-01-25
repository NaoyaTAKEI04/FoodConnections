from django.urls import path
from .views import CustomSignupView

urlpatterns = [
    path('accounts/signup/', CustomSignupView.as_view(), name='account_signup'),
]