from allauth.account.forms import SignupForm
from django import forms

class CustomSignupForm(SignupForm):
    user_type = forms.ChoiceField(
        choices=[
            ('general', '一般ユーザー'),
            ('restaurant_owner', '飲食店オーナー'),
            ('farmer', '農家'),
        ],
        label='ユーザータイプ',
    )