from django.urls import path, include
from django.contrib import admin
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
<<<<<<< HEAD
    path('', views.landingpage, name="landingpage"),
    path('filelist/', views.file_list, name="filelist")
    
=======
    path('', views.index_view, name="landingpage"),
    path('filelist/', views.FileListView.as_view(), name="file-list"),
    path('filelist/file-add/', views.fileadd, name="file-add"),
<<<<<<< HEAD
    path('folder-add/', views.folderadd, name="folder-add")
>>>>>>> Upload file seems to work
=======
    path('filelist/folder-add/', views.folderadd, name="folder-add")
>>>>>>> Create folder seems to work

]



if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
