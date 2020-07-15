from django.urls import path, include
from django.contrib import admin
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index_view, name="landingpage"),
    path('filelist/', views.FileListView.as_view(), name="file-list"),
    path('filelist/file-add/', views.fileadd, name="file-add"),
    path('folder-add/', views.folderadd, name="folder-add")

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
