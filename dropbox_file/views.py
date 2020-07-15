from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib import messages
from django.views.generic import ListView


from .models import FileObject
from .forms import AddFileForm, AddFolderForm


def index_view(request):
    return render(request, 'landingpage.html')


class FileListView(ListView):
    model = FileObject
    context_object_name = 'files'
    template_name = 'filelist.html'


def fileadd(request):
    html = 'general_form.html'
    form = AddFileForm()
    if request.method == "POST":
        form = AddFileForm(request.POST, request.FILES)
        if form.is_valid():
            new_file = form.save(commit=False)
            new_file.uploaded_by = request.user
            new_file.save()
            messages.info(request, "File created successfully!")
            return HttpResponseRedirect(reverse('file-list'))
        else:
            form = AddFileForm()
    return render(request, html, {"form": form})


def folderadd(request):
    html = 'general_form.html'
    form = AddFolderForm()
    if request.method == "POST":
        form = AddFolderForm(request.POST, request.FILES)
        if form.is_valid():
            new_file = form.save(commit=False)
            new_file.uploaded_by = request.user
            new_file.save()
            messages.info(request, "Folder created successfully!")
            return HttpResponseRedirect(reverse('file-list'))
        else:
            form = AddFileForm()
    return render(request, html, {"form": form})
