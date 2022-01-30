from django.db import models

# Create your models here.
class Pegawai (models.Model):
    nip = models.CharField(max_length=18, primary_key=True)
    name = models.CharField(max_length=100)
    bidang = models.CharField(max_length=50)
    seksi = models.CharField(max_length=50)
    jabatan = models.CharField(max_length=50)