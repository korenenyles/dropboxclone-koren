from django import forms
from django.contrib.auth.forms import UserCreationForm
from dropbox_user.models import DropBoxUser

class LoginForm(forms.Form):
    email = forms.EmailField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput)

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=60,
        help_text="A valid email address is required")

    class Meta:
        model = DropBoxUser
        fields = ('email', 'password1', 'password2', 'username')

# class SignUpForm(forms.Form):
#     email = forms.EmailField(max_length=30)
#     password1 = forms.CharField(widget=forms.PasswordInput)
#     password2 = forms.CharField(label='Matching Password',
#                                 widget=forms.PasswordInput)
#     username = forms.CharField(max_length=30)

