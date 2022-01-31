# from mr.models import IndikatorRisikoUtama
from kasus.models import Kasus
# from mr.proc import periode_IRU, periode_RA
# from manajemenrisiko.tools import connDB
# from pegawai.proc import getPegawai


def getKasus():
    kasus = Kasus.objects.all()
    return kasus