# Generated by Django 3.0.7 on 2022-01-31 09:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pegawai', '0002_users'),
    ]

    operations = [
        migrations.CreateModel(
            name='OperatorConsole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tahun', models.IntegerField(null=True)),
                ('kep', models.CharField(max_length=100, null=True)),
                ('nip', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pegawai.Pegawai')),
            ],
        ),
        migrations.DeleteModel(
            name='Users',
        ),
    ]
