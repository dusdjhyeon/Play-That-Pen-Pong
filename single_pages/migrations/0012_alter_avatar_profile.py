# Generated by Django 4.0.3 on 2022-07-03 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('single_pages', '0011_alter_avatar_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avatar',
            name='profile',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]