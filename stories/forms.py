from django import forms
from .models import Contact, Comment

# class ContactForm(forms.Form):
#     first_name = forms.CharField(max_length = 20)
#     last_name = forms.CharField(max_length = 20)
#     message = forms.CharField(max_length = 50)

class ContactForm(forms.ModelForm):
    #possible to create additional fields here
    name = forms.CharField(label='', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Your Name'
    }), max_length=30)
    email = forms.EmailField(label='', widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Your Email'
    }),)
    subject = forms.CharField(label='', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Subject'
    }),max_length=60)
    message = forms.CharField(label='', widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Message',
        'cols': '30',
        'rows': '7',
    }),)

    class Meta:
        model = Contact
        fields = '__all__'
        # fields = ('message',) #if you want to choose specific fields to show
        # exclude = ('message',)

class CommentForm(forms.ModelForm):
    comment = forms.CharField(label='Your Comment', widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Leave your comment here',
        'cols': '30',
        'rows': '7',
    }),)
    class Meta:
        model = Comment
        fields = ['comment',]