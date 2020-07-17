from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FileObject',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(max_length=50, unique=True)),
                ('uploaded_file', models.FileField(
                    blank=True, null=True, upload_to='uploads/')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(
                    db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True,
                                                      on_delete=django.db.models.deletion.CASCADE, related_name='children', to='dropbox_file.FileObject')),
                ('uploaded_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                                  related_name='uploader', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
