from django.shortcuts import render, redirect
from kasus.proc import *

# Create your views here.
def tambah_kasus_view(request):
    template = "kasus/template/tambah_kasus.html"
    context = {}
    context["title"] = "Tambah Kasus"
    if request.method == "POST":
        data_kasus = {}
        data_kasus["pelapor"] = request.user
        data_kasus["device"] = request.POST["idDevice"]
        data_kasus["deskripsi"] = request.POST["deskripsi"]
        tambah_kasus(data_kasus)
        return redirect("/home")
    return render(request, template, context)

def update_kasus_view(request, idKasus):
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