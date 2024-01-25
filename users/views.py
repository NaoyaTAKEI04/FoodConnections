from allauth.account.views import SignupView
from .forms import CustomSignupForm

class CustomSignupView(SignupView):
    form_class = CustomSignupForm

    def form_valid(self, form):
        form.instance.user_type = form.cleaned_data['user_type'] # フォームの保存前にユーザータイプを設定
        return super().form_valid(form) # ユーザー登録が成功した後、デフォルトの処理を続行
