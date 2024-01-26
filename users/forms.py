from allauth.account.forms import SignupForm
from django import forms
from .models import CustomUser

class CustomSignupForm(SignupForm):
    USER_TYPE_CHOICES = (
        ('general', '一般ユーザー'),
        ('restaurant_owner', '飲食店オーナー'),
        ('farmer', '農家'),
    )
    user_type = forms.ChoiceField(choices=USER_TYPE_CHOICES,label='ユーザータイプ',)

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.user_type = self.cleaned_data['user_type']
        user.save()
        return user