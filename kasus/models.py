from django.db import models
from pegawai.models import Pegawai, OperatorConsole

# Create your models here.
def user_directory_path(instance, filename):
    return "user_{}/{}".format(instance.user.id, filename)

class Device(models.Model):
    idDevice = models.AutoField(primary_key=True)
    jenis = models.CharField(max_length=50)
    keterangan = models.TextField()
    noBMN = models.CharField(max_length=100)

class Kasus(models.Model):
    idKasus = models.AutoField(primary_key=True)
    tanggal = models.DateField()
    pelapor = models.ForeignKey(to=Pegawai, on_delete=models.SET_NULL, null=True)
    device = models.ForeignKey(to=Device, on_delete=models.SET_NULL, null=True)
    buktiFoto = models.FileField(upload_to=user_directory_path, null = True)
    penindaklanjut = models.ForeignKey(to=OperatorConsole, on_delete=models.SET_NULL, null=True)
    progres = models.TextField(null=True)
    status = models.CharField(max_length=50, null=True)
    deskripsi = models.TextField(null=True)
    tanggal_update = models.DateField(null=True)