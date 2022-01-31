from kasus.models import *
from datetime import date
from pegawai.models import *
from pegawai.proc import is_oc


def tambah_kasus(data_kasus):
    pegawai = Pegawai.objects.get(nip = data_kasus["pelapor"])
    device = Device.objects.get_or_create(idDevice = data_kasus["device"])[0]
    k = Kasus(
        tanggal = date.today(),
        pelapor = pegawai,
        device = device,
        deskripsi = data_kasus["deskripsi"],
        status = "Open",
    )
    k.save()

def update_kasus(progres):
    if not is_oc(progres["nip"]):
        return
    kasus = Kasus.objects.get(idKasus = progres["idKasus"])
    penindaklanjut = OperatorConsole.objects.get(nip=Pegawai.objects.get(nip=progres["nip"]))
    kasus.progres = progres["progres"]
    kasus.status = progres["status"]
    kasus.penindaklanjut = penindaklanjut
    kasus.tanggal_update = date.today()
    kasus.save()