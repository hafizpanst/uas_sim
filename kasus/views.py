from django.shortcuts import render, redirect
from kasus.proc import *

# Create your views here.
def tambah_kasus_view(request):
    try:
        template = "kasus/template/tambah_kasus.html"
        context = {}
        context["title"] = "Tambah Kasus"
        if request.method == "POST":
            data_kasus = {}
            data_kasus["pelapor"] = request.user
            data_kasus["noBMN"] = request.POST["noBMN"]
            data_kasus["deskripsi"] = request.POST["deskripsi"]
            tambah_kasus(data_kasus)
            return redirect("/home")
        return render(request, template, context)
    except:
        redirect("/home/404")

def update_kasus_view(request, idKasus):
    try:
        kasus = Kasus.objects.get(idKasus = idKasus)
        if kasus.status == "Close":
            return redirect("/home")
        if not is_oc(request.user):
            return redirect("/home")
        template = "kasus/template/update_kasus.html"
        context = {}
        context["title"] = "Update Kasus"
        if request.method == "POST":
            progres = {}
            progres["nip"] = request.user
            progres["idKasus"] = idKasus
            progres["progres"] = request.POST["progres"]
            progres["status"] = request.POST["status"]
            update_kasus(progres)
            return redirect("/home")
        context["kasus"] = Kasus.objects.get(idKasus=idKasus)
        return render(request, template, context)
    except:
        redirect("/home/404")

def cari_kasus_view(request):
    try:
        template = "kasus/template/cari_kasus.html"
        context = {}
        context["title"] = "Cari Kasus"
        if request.method == "POST":
            data_kasus = {}
            if request.POST["key"] == "pelapor":
                data_kasus["key"] = "pelapor"
                data_kasus["pelapor"] = request.POST["keyword"]
            elif request.POST["key"] == "deskripsi":
                data_kasus["key"] = "deskripsi"
                data_kasus["deskripsi"] = request.POST["keyword"]
            daftar_kasus = cari_kasus(data_kasus)
            context["daftar_kasus"] = daftar_kasus
        return render(request, template, context)
    except:
        redirect("/home/404")

def tambah_device_view(request):
    if not is_oc(request.user):
        return redirect("/home")
    try:
        template="kasus/template/tambah_device.html"
        context={}
        context["title"]="Tambah Device"
        if request.method == "POST":
            data_device={}
            data_device["noBMN"]=request.POST["noBMN"]
            data_device["jenis"]=request.POST["jenis"]
            data_device["keterangan"]=request.POST["keterangan"]
            valid = tambah_device(data_device)
            if valid:
                return redirect("/home")
            else:
                print("valid:", valid)
                return redirect("/home/404")
        return render(request, template, context)
    except Exception as e:
        print(e)
        return redirect("/home/404")
