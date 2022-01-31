from random import choice
from django.db import models

# Create your models here.
class Pegawai(models.Model):
    nip = models.CharField(max_length=18, primary_key=True)
    name = models.CharField(max_length=100)
    bidang = models.CharField(max_length=50)
    seksi = models.CharField(max_length=50)
    jabatan = models.CharField(max_length=50)

class OperatorConsole(models.Model):
    nip = models.ForeignKey(to=Pegawai, on_delete=models.SET_NULL, null=True)
    tahun = models.IntegerField(null=True)
    kep = models.CharField(max_length=100, null=True)