from django.shortcuts import render, redirect
from pegawai.proc import *
# from django.contrib.auth import authenticate, login, logout

# Create your views here.
def login_view(request):
    try:
        template = "pegawai/template/login.html"
        context = {}
        if request.method == "POST":
            username = request.POST["username"]
            password = request.POST["password"]
            request, valid = login_pegawai(request=request, nip=username, password=password)
            if not valid:
                return redirect("/pegawai/login")
            return redirect("/home")
        return render(request, template, context)
    except:
        return redirect("/home/404")

def logout_view(request):
    logout_pegawai(request)
    return redirect("/pegawai/login")

def register_view(request):
    try:
        template = "pegawai/template/register.html"
        context = {}
        if request.method == "POST":
            username = request.POST["username"]
            password = request.POST["password"]
            registrasi = registrasi_pegawai(nip=username, password=password)
            if registrasi:
                return redirect("/pegawai/login")
            else:
                print(registrasi)
                return redirect("/home/404")
        return render(request, template, context)
    except Exception as e:
        print("error: ", e)
        return redirect("/home/404")

def tambah_pegawai_view(request):
    if not is_oc(request.user):
        return redirect("/home")
    try:
        template="pegawai/template/tambah_pegawai.html"
        context={}
        context["title"] = "Tambah Pegawai"
        if request.method == "POST":
            data_pegawai={}
            data_pegawai["nip"]=request.POST["nip"]
            data_pegawai["name"]=request.POST["name"]
            data_pegawai["bidang"]=request.POST["bidang"]
            data_pegawai["seksi"]=request.POST["seksi"]
            data_pegawai["jabatan"]=request.POST["jabatan"]
            valid=tambah_pegawai(data_pegawai)
            if valid:
                return redirect("/pegawai/tambah_pegawai")
            else:
                return redirect("/home/404")
        return render(request, template, context)
    except:
        return redirect("/home/404")

def tambah_oc_view(request):
    if not is_oc(request.user):
        return redirect("/home")
    try:
        template="pegawai/template/tambah_oc.html"
        context={}
        context["title"] = "Tambah Operator Console"
        if request.method == "POST":
            data_oc={}
            data_oc["nip"]=request.POST["nip"]
            data_oc["tahun"]=int(request.POST["tahun"])
            data_oc["kep"]=request.POST["kep"]
            valid=tambah_oc(data_oc)
            if valid:
                return redirect("/pegawai/tambah_oc")
            else:
                return redirect("/home/404")
        return render(request, template, context)
    except:
        return redirect("/home/404")
