from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from allauth.account.views import SignupView
from .forms import CustomSignupForm, ProfileEditForm

class CustomSignupView(SignupView):
    form_class = CustomSignupForm

    def form_valid(self, form):
        # ユーザー登録が成功した後、何もせずに元の処理を続行
        return super().form_valid(form)

@login_required
def profile_edit_view(request):
    if request.method == 'POST':
        form = ProfileEditForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileEditForm(instance=request.user)
    return render(request, 'profile_edit.html', {'form': form})
