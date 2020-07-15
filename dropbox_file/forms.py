from mptt.forms import forms
from .models import FileObject
from django.forms import ModelForm


class AddFolderForm(forms.Form):
    filename = forms.CharField(max_length=50, help_text='*Required')
    parent = forms.ModelChoiceField(queryset=FileObject.objects.all())


# Citation:
# https://docs.djangoproject.com/en/3.0/topics/forms/modelforms/
# https://stackoverflow.com/questions/23718484/django-assign-default-value-to-field-in-modelform
class AddFileForm(ModelForm):
    class Meta:
        model = FileObject
        fields = ['filename', 'uploaded_file', 'parent']
        exclude = ['uploaded_by']

# Just in case my ModelForm isn't working...

# class AddFileForm(forms.Form):
#     filename = forms.CharField(max_length=50, help_text='*Required')
#     uploaded_file = forms.FileField(help_text='*Required')
#     parent = forms.ModelChoiceField(queryset=FileObject.objects.all())
