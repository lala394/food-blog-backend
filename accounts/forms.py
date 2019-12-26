from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.forms import UsernameField
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import PasswordChangeForm

User = get_user_model()

class CustomLoginForm(AuthenticationForm):
    username = UsernameField(label="", widget=forms.TextInput(attrs={
        'autofocus':True,
        'class': 'form-control' , 
        'placeholder': 'Username',       
        }))
    password = forms.CharField(
        label="",
        strip=False,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Password',
        }),
    )

class CustomRegisterForm(UserCreationForm):
    first_name = forms.CharField(widget = forms.TextInput(attrs={
        'class':'form-control',
        'placeholder': 'First name'
    }))
    last_name = forms.CharField(widget = forms.TextInput(attrs={
        'class':'form-control',
        'placeholder': 'Last name'
    }))
    username = UsernameField(widget = forms.TextInput(attrs={
        'class':'form-control',
        'placeholder': 'Username'
    }))
    email = forms.CharField(widget = forms.EmailInput(attrs={
        'class':'form-control',
        'placeholder': 'E-mail'
    }))
    password1 = forms.CharField(widget = forms.PasswordInput(attrs={
        'class':'form-control',
        'placeholder': 'Password'
    }))
    password2 = forms.CharField(widget = forms.PasswordInput(attrs={
        'class':'form-control',
        'placeholder': 'Confirm password'
    }))

    class Meta:
        model = User
        fields = ['first_name', 'last_name','username', 'email', 'password1', 'password2']


class CustomChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(widget = forms.PasswordInput(attrs={
    'class':'form-control',
    'placeholder': 'Old Password'
    }))
    new_password1 = forms.CharField(widget = forms.PasswordInput(attrs={
    'class':'form-control',
    'placeholder': 'New Password'
    }))
    new_password2 = forms.CharField(widget = forms.PasswordInput(attrs={
    'class':'form-control',
    'placeholder': 'Confirm Password'
    }))
    class Meta:
        fields=[
            'old_password',
            'new_password1',
            'new_password2',
        ]