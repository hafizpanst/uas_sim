# Generated by Django 3.0.7 on 2022-01-30 10:29

from django.db import migrations, models
import kasus.models


class Migration(migrations.Migration):

    dependencies = [
        ('kasus', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='kasus',
            name='buktiFoto',
            field=models.FileField(null=True, upload_to=kasus.models.user_directory_path),
        ),
    ]
