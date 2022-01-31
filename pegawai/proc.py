from pegawai.models import Pegawai
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from pegawai.models import OperatorConsole


def registrasi_pegawai(nip, password):
    try:
        pegawai = Pegawai.objects.filter(nip = nip)
        if len(pegawai) != 0:
            user = User.objects.create_user(username = nip, password = password)
            user.save()
            return True
    except Exception as e:
        print(e)
    return False

def login_pegawai(request, nip, password):
    try:
        user = authenticate(request, username = nip, password = password)
        login(request, user)
        request.session.set_expiry(0)
        return request, True
    except Exception as e:
        return request, False

def logout_pegawai(request):
    logout(request)
    return request

def is_oc(nip):
    pegawai = Pegawai.objects.get(nip=nip)
    oc = OperatorConsole.objects.filter(nip=pegawai)
    if len(oc) != 0:
        return True
    return False