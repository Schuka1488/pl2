from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

class AddReviews(forms.ModelForm):

    emailBuyerAccount = forms.EmailField(label='Email', widget=forms.EmailInput)
    class Meta:
        model = Review
        fields = ['starReview', 'textReview', 'nameReview', 'emailBuyerAccount']

        widgets = {
            'textReview': forms.Textarea(attrs={'cols': 60, 'rows': 5}),
            'nameReview': forms.Textarea(attrs={'cols': 23, 'rows': 1}),
            'emailBuyerAccount': forms.Textarea(attrs={'cols': 60, 'rows': 1}),
        }

class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput)
    email = forms.EmailField(label='Email', widget=forms.EmailInput)
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput)
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'password']
