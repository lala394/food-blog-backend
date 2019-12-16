from django.urls import path, include
from .views import *

app_name = 'accounts'

urlpatterns = [
    # path('login/', login, name='login' ),
    path('login/', CustomLoginView.as_view(), name='login' ),
    path('change-password', change_password, name='change-password'),
    path('reset-password', reset_password, name='reset-password'),
    # path('register', register, name='register'),
    path('register', CustomRegisterView.as_view(), name='register'),
    path('forget-password', forget_password, name='forget-password'),

]