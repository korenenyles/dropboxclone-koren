from django.shortcuts import render
from dropbox_user.models import DropBoxUser
from dropbox_file.models import FileObject

# Create your views here.
def userpage(request, id):
    dropbox_user = DropBoxUser.objects.get(id=id)
    filename = FileObject.objects.filter(id=id)
    return render(request, 'userpage.html',
        {"dropbox_user": dropbox_user, "filename": filename})

