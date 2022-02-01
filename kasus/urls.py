from django.urls import path
from kasus.views import *

urlpatterns = [
    path("tambah_kasus", tambah_kasus_view),
    path("update_kasus/<int:idKasus>", update_kasus_view),
    path("cari_kasus", cari_kasus_view),
    path("tambah_device", tambah_device_view),
]