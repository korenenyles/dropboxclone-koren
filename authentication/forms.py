from django import forms

class LoginForm(forms.Form):
    email = forms.EmailField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput)

class SignUpForm(forms.Form):
    email = forms.EmailField(max_length=30)
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(label='Matching Password',
                                widget=forms.PasswordInput)
    username = forms.CharField(max_length=30)

