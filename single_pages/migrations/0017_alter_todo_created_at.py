# Generated by Django 4.0.3 on 2022-07-13 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('single_pages', '0016_todo_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='created_at',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
