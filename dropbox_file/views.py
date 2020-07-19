from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib import messages
<<<<<<< HEAD
from .models import FileObject
from .forms import AddFileForm, AddFolderForm
from django.views.generic import ListView, CreateView, \
    UpdateView
=======
from django.views.generic import ListView
from .models import FileObject
from .forms import AddFileForm, AddFolderForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from dropbox_user.models import DropBoxUser
>>>>>>> 67e91d8a76aaf97b7b4bc080c819c5129bf37aba

@login_required
def landingpage(request):
    user_data = DropBoxUser.objects.all()
    return render(request, 'landingpage.html', {user_data: 'user_data'})


# error views for custom error pages

def error_404(request, exception):
    return render(request, '404.html', status=404)


def error_500(request):
    return render(request, '500.html', status=500)

<<<<<<< HEAD

# This should count for a FileObject.objects.all()
=======
@method_decorator(login_required, name='dispatch')
>>>>>>> 67e91d8a76aaf97b7b4bc080c819c5129bf37aba
class FileListView(ListView):
    
    model = FileObject
    context_object_name = 'files'
    template_name = 'filelist.html'


<<<<<<< HEAD
class AddFileView(CreateView):
    model = FileObject
    fields = ('filename', 'uploaded_file', 'parent')
    template_name = 'general_form.html'

    def post(self, request):
=======
def fileadd(request):
    
    html = 'general_form.html'
    form = AddFileForm()
    if request.method == "POST":
>>>>>>> 67e91d8a76aaf97b7b4bc080c819c5129bf37aba
        form = AddFileForm(request.POST, request.FILES)
        if form.is_valid():
            new_file = form.save(commit=False)
            new_file.uploaded_by = request.user
            new_file.save()
            messages.info(request, "File created successfully!")
            return HttpResponseRedirect(reverse('filelist'))
        else:
            form = AddFileForm()
        return render(request, {"form": form})


<<<<<<< HEAD
class AddFolderView(CreateView):
    model = FileObject
    fields = ('filename', 'parent')
    template_name = 'general_form.html'

    def post(self, request):
        form = AddFolderForm(request.POST)
=======
@login_required
def folderadd(request):
    html = 'general_form.html'
    form = AddFolderForm()
    if request.method == "POST":
        form = AddFolderForm(request.POST, request.FILES)
>>>>>>> 67e91d8a76aaf97b7b4bc080c819c5129bf37aba
        if form.is_valid():
            new_file = form.save(commit=False)
            new_file.uploaded_by = request.user
            new_file.save()
            messages.info(request, "Folder created successfully!")
            return HttpResponseRedirect(reverse('filelist'))
        else:
            form = AddFolderForm()
        return render(request, {"form": form})


class EditFileView(UpdateView):
    model = FileObject
    template_name = "general_form.html"
    fields = ('filename', 'parent')
    success_url = '/filelist'


# Citation:
# https://stackoverflow.com/questions/19754103/django-how-to-delete-an-object-using-a-view
def file_delete(request, id):
    requested_file = FileObject.objects.get(id=id)
    requested_file.delete()
    messages.info(request, "File deleted successfully!")
    return HttpResponseRedirect(reverse('filelist'))