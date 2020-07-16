from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib import messages
from django.views.generic import ListView, CreateView


from .models import FileObject
from .forms import AddFileForm, AddFolderForm


def landingpage(request):
    return render(request, 'landingpage.html')


# error views for custom error pages

def error_404(request, exception):
    return render(request, '404.html', status=404)


def error_500(request):
    return render(request, '500.html', status=500)


class FileListView(ListView):
    model = FileObject
    context_object_name = 'files'
    template_name = 'filelist.html'


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
