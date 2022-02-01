from webbrowser import Opera
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

def tambah_pegawai(data_pegawai):
    if len(Pegawai.objects.filter(nip=data_pegawai["nip"])) != 0:
        return False
    p = Pegawai(
        nip=data_pegawai["nip"],
        name=data_pegawai["name"],
        bidang=data_pegawai["bidang"],
        seksi=data_pegawai["seksi"],
        jabatan=data_pegawai["jabatan"],
    )
    p.save()
    return True

def tambah_oc(data_oc):
    if len(Pegawai.objects.filter(nip=data_oc["nip"])) == 0 or is_oc(data_oc["nip"]):
        return False
    
    oc = OperatorConsole(
        nip=Pegawai.objects.get(nip=data_oc["nip"]),
        tahun=data_oc["tahun"],
        kep=data_oc["kep"],
    )
    oc.save()
    return True