"""DropBox_Mptt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls import handler404, handler500
from dropbox_user.urls import urlpatterns as user_urls
from dropbox_file.urls import urlpatterns as file_urls
from authentication.urls import urlpatterns as auth_urls
from dropbox_file import views as error_views
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
   
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = error_views.error_404
handler500 = error_views.error_500


urlpatterns += user_urls
urlpatterns += file_urls
urlpatterns += auth_urls
