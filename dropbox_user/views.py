from django.shortcuts import render
from dropbox_user.models import DropBoxUser
from dropbox_file.models import FileObject
from django.contrib.auth.decorators import login_required

__author__ = ["mprodhan", "korennyles", "MalikMAlna"]
# Create your views here.
@login_required
def userpage(request, id):
    dropbox_user = DropBoxUser.objects.get(id=id)
    filename = FileObject.objects.filter(id=id)
    return render(request, 'userpage.html',
        {"dropbox_user": dropbox_user, "filename": filename})

