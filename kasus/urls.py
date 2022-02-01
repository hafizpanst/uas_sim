from django.urls import path
from kasus.views import *

urlpatterns = [
    # path("input_kejadian_risiko/", input_kejadian_risiko_view),
    # path("input_rencana_aksi/", input_rencana_aksi_view),
    # path("input_indikator_risiko_utama/", input_indikator_risiko_utama_view),
    # path("indikator_risiko_utama", indikator_risiko_utama_view),
    # path("indikator_risiko_utama/<int:id_iru>", nilai_aktual_iru_view),
    # path("rencana_aksi", rencana_aksi_view),
    # path("rencana_aksi/<int:id_rencana_aksi>", pelaksanaan_rencana_aksi_view),
    # path("import_pelaksanaan_rencana_aksi", import_pelaksanaan_rencana_aksi_view),
    path("tambah_kasus", tambah_kasus_view),
    path("update_kasus/<int:idKasus>", update_kasus_view),
    path("cari_kasus", cari_kasus_view),
]