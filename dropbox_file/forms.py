from mptt.forms import forms
from .models import FileObject


class AddFolderForm(forms.Form):
    filename = forms.CharField(max_length=50, help_text='*Required')
    parent = forms.ModelChoiceField(queryset=FileObject.objects.all())


class AddFileForm(forms.Form):
    filename = forms.CharField(max_length=50, help_text='*Required')
    uploaded_file = forms.FileField(help_text='*Required')
    parent = forms.ModelChoiceField(queryset=FileObject.objects.all())
