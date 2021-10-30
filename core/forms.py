from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    name = forms.CharField(max_length=50, required=False)
    email = forms.EmailField(max_length=254)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput())

    class Meta:
        model = User
        help_texts = {
            'username': None,
        }
        fields = ('username', 'name', 'email', 'password1', 'password2', )