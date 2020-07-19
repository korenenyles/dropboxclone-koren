from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib import messages
from .models import FileObject
from .forms import AddFileForm, AddFolderForm
from django.views.generic import ListView, CreateView, \
    UpdateView
from dropbox_user.models import DropBoxUser
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

@login_required
def landingpage(request):
    user_data = DropBoxUser.objects.all()
    return render(request, 'landingpage.html', {user_data: "user_data"})


# error views for custom error pages

def error_404(request, exception):
    return render(request, '404.html', status=404)


def error_500(request):
    return render(request, '500.html', status=500)

@method_decorator(login_required, name='dispatch')
# This should count for a FileObject.objects.all()
class FileListView(ListView):
    model = FileObject
    context_object_name = 'files'
    template_name = 'filelist.html'

@method_decorator(login_required, name='dispatch')
class AddFileView(CreateView):
    model = FileObject
    fields = ('filename', 'uploaded_file', 'parent')
    template_name = 'general_form.html'

    def post(self, request):
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

@method_decorator(login_required, name='dispatch')
class AddFolderView(CreateView):
    model = FileObject
    fields = ('filename', 'parent')
    template_name = 'general_form.html'

    def post(self, request):
        form = AddFolderForm(request.POST)
        if form.is_valid():
            new_file = form.save(commit=False)
            new_file.uploaded_by = request.user
            new_file.save()
            messages.info(request, "Folder created successfully!")
            return HttpResponseRedirect(reverse('filelist'))
        else:
            form = AddFolderForm()
        return render(request, {"form": form})

@method_decorator(login_required, name='dispatch')
class EditFileView(UpdateView):
    model = FileObject
    template_name = "general_form.html"
    fields = ('filename', 'parent')
    success_url = '/filelist'


# Citation:
# https://stackoverflow.com/questions/19754103/django-how-to-delete-an-object-using-a-view
@login_required
def file_delete(request, id):
    requested_file = FileObject.objects.get(id=id)
    requested_file.delete()
    messages.info(request, "File deleted successfully!")
    return HttpResponseRedirect(reverse('filelist'))
