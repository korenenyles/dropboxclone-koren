from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin

from dropbox_file.models import FileObject

admin.site.register(FileObject, DraggableMPTTAdmin)
