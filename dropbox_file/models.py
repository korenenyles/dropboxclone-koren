from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from dropbox_user.models import DropBoxUser


class FileObject(MPTTModel):
    filename = models.CharField(max_length=50, unique=True)
    uploaded_by = models.ForeignKey(
        DropBoxUser,
        related_name="uploader",
        on_delete=models.CASCADE
    )
    uploaded_file = models.FileField(
        blank=True, null=True, upload_to='files/')
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="children"
    )

    class MPTTMeta:
        order_insertion_by = ['filename']

    def __str__(self):
        return self.filename
