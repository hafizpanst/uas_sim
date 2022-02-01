from django.urls import path
from pegawai.views import *

urlpatterns = [
    path("register", register_view),
    path("login", login_view),
    path("logout", logout_view),
    path("tambah_pegawai", tambah_pegawai_view),
    path("tambah_oc", tambah_oc_view),
]