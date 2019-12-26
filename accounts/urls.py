from django.urls import path, include
from .views import *
from django.contrib.auth.views import LogoutView, PasswordChangeView

app_name = 'accounts'

urlpatterns = [
    # path('login/', login, name='login' ),
    path('login/', CustomLoginView.as_view(), name='login' ),
    path('logout/', LogoutView.as_view(), name="logout"),
    # path('change-password', change_password, name='change-password'),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('reset-password/', reset_password, name='reset-password'),
    # path('register', register, name='register'),
    path('register/', CustomRegisterView.as_view(), name='register'),
    path('forget-password/', forget_password, name='forget-password'),
    path('password-change-done/', ChangePasswordDone.as_view(), name='password_change_done')

]