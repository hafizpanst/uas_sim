from django.urls import path
from pegawai.views import *

urlpatterns = [
    path("register", register_view),
    path("login", login_view),
    path("logout", logout_view),
]