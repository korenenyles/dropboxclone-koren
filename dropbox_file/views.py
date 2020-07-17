from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib import messages
from django.views.generic import ListView
from .models import FileObject
from .forms import AddFileForm, AddFolderForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from dropbox_user.models import DropBoxUser

@login_required
def landingpage(request):
    user_data = DropBoxUser.objects.all()
    return render(request, 'landingpage.html', {user_data: 'user_data'})


# error views for custom error pages

def error_404(request, exception):
    return render(request, '404.html', status=404)


def error_500(request):
    return render(request, '500.html', status=500)

@method_decorator(login_required, name='dispatch')
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
            return HttpResponseRedirect(reverse('filelist'))
        else:
            form = AddFileForm()
    return render(request, html, {"form": form})

@login_required
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
            return HttpResponseRedirect(reverse('filelist'))
        else:
            form = AddFileForm()
    return render(request, html, {"form": form})
