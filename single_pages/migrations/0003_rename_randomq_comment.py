# Generated by Django 4.0.3 on 2022-04-06 16:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('single_pages', '0002_remove_post_file_upload_remove_post_head_image'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='randomQ',
            new_name='Comment',
        ),
    ]