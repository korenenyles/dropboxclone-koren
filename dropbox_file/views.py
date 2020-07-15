from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib import messages
from django.views.generic import ListView


from .models import FileObject
from .forms import AddFileForm, AddFolderForm


<<<<<<< HEAD
# Create your views here.
def landingpage(request):
    return render(request, 'landingpage.html')

def file_list(request):
        return render(request, 'filelist.html')

        


# error views for custom error pages 

def error_404(request, exception):
        return render(request,'404.html', status=404)

def error_500(request):
        return render(request,'500.html', status=500)


=======
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
        form = AddFolderForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            FileObject.objects.create(
                filename=data['filename'],
                parent=data['parent']
            )
            messages.info(request, "Folder created successfully!")
            return HttpResponseRedirect(reverse('filelist'))

    return render(request, html, {"form": form})
>>>>>>> Upload file seems to work
