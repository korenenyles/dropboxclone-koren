from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',
         views.landingpage,
         name="landingpage"),
    path('filelist/',
         views.FileListView.as_view(),
         name="filelist"),
    path('file_object/<int:pk>',
         views.FileDetailView.as_view(),
         name='file-detail'),
    path('filelist/file-add/',
         views.AddFileView.as_view(),
         name="file-add"),
    path('filelist/folder-add/',
         views.AddFolderView.as_view(),
         name="folder-add"),
    path('file/edit/<int:pk>',
         views.EditFileView.as_view(),
         name='file-edit'),
    path('file/delete/<int:id>',
         views.file_delete,
         name='file-delete'),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
