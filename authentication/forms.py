from django import forms

class LoginForm(forms.Form):
    email = forms.EmailField(max_length=30, unique=True)
    password = forms.CharField(widget=forms.PasswordInput)

class SignUpForm(forms.Form):
    email = forms.EmailField(max_length=30, unique=True)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.Charfield(label='Matching Password', 
                                        widget=forms.PasswordInput)