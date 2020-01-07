from django.urls import path, include, re_path
from .views import *
from django.contrib.auth.views import LogoutView, PasswordChangeView

app_name = 'accounts'

urlpatterns = [
    # path('login/', login, name='login' ),
    # path('change-password', change_password, name='change-password'),
    # path('reset-password/', reset_password, name='reset-password'),
    # path('register', register, name='register'),
    # path('forget-password/', forget_password, name='forget-password'),
    path('login/', CustomLoginView.as_view(), name='login' ),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('reset-password/', ResetPasswordView.as_view(), name='reset-password'),
    path('register/', CustomRegisterView.as_view(), name='register'),
    path('password-change-done/', ChangePasswordDone.as_view(), name='password_change_done'),
    re_path(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
]