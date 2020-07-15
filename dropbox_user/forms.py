from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from dropbox_user.models import DropBoxUser, DropBoxUserManager
from dropbox_user.forms import DropBoxUserAdminForm


class LoginFormCreation(forms.ModelForm):
    password = forms.CharrField(widget=forms.PasswordInput)
    confirm_password = forms.Charfield(label='Matching Password',
                                       widget=forms.PasswordInput)

    class Meta:
        Model = DropBoxUser
        fields = ('email', 'display name')

    def email_validation(self):
        email = self.cleaned_data.get('email')
        display_name = self.cleaned_data.get('display name')
        qs = DropBoxUser.objects.filter(email=email,
                                        display_name=display_name)
        if qs.exists():
            raise forms.ValidationError('email is taken')
        return email, display_name

    def password_validation(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('matching password')
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError('Passwords do not match')
        return confirm_password


class AdminLoginFormCreation(forms.ModelForm):
    password = forms.CharrField(widget=forms.PasswordInput)
    confirm_password = forms.Charfield(label='Matching Password',
                                       widget=forms.PasswordInput)

    class Meta:
        Model = DropBoxUser
        fields = ('email', 'display name')

    def password_validation(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('matching password')
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError('Passwords do not match')
        return confirm_password

    def hash_password(self, commit=True):
        dropbox_user = super(DropBoxUserAdminForm, self).save(commit=False)
        dropbox_user.set_password(self.cleaned_data['password'])
        if commit:
            dropbox_user.save()
        return dropbox_user


class DropBoxUserAdminChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField

    class Meta:
        Model = DropBoxUser
        fields = ('email', 'display name', 'password', 'active', 'admin')

    def init_password(self):
        return self.initial['password']
