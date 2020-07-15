from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.landingpage, name="landingpage"),
    path('filelist/', views.FileListView.as_view(), name="file-list"),
    path('filelist/file-add/', views.fileadd, name="file-add"),
    path('filelist/folder-add/', views.folderadd, name="folder-add"),

]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
