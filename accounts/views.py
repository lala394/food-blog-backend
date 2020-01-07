from django.shortcuts import render
from django.contrib.auth.views import LoginView
from .forms import CustomLoginForm, CustomRegisterForm, CustomChangePasswordForm, CustomSetPasswordForm, CustomResetPasswordForm
from django.views.generic import CreateView
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
User = get_user_model()
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView, PasswordResetView, PasswordResetForm, PasswordResetConfirmView


# Create your views here.

def change_password(request):
    return render(request, 'change_password.html')

class ChangePasswordView(PasswordChangeView):
    template_name = 'change_password.html'
    form_class = CustomChangePasswordForm
    success_url = reverse_lazy('accounts:password_change_done')

class ChangePasswordDone(PasswordChangeDoneView):
    template_name = 'password_change_done.html'


# def forget_password(request):
#     return render(request, 'forget_password.html')

class ResetPasswordView(PasswordResetView):
    form_class = CustomResetPasswordForm
    template_name = 'forget_password.html'
    email_template_name = 'password_reset_email.html'
    success_url = reverse_lazy('stories:home')


class CustomLoginView(LoginView):
    template_name = 'login.html'
    form_class = CustomLoginForm

# def login(request):
#     return render(request, 'login.html')

# def register(request):
#     return render(request, 'register.html')

class CustomRegisterView(CreateView):
    model = User
    template_name = 'register.html'
    form_class = CustomRegisterForm
    success_url = reverse_lazy('accounts:login')


# def reset_password(request):
#     return render(request, 'reset_password.html')

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'reset_password.html'
    form_class = CustomSetPasswordForm
    success_url = reverse_lazy('accounts:login')
