# Generated by Django 3.0.7 on 2022-01-30 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pegawai',
            fields=[
                ('nip', models.CharField(max_length=18, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('bidang', models.CharField(max_length=50)),
                ('seksi', models.CharField(max_length=50)),
                ('jabatan', models.CharField(max_length=50)),
            ],
        ),
    ]
