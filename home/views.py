from datetime import datetime
from home.proc import *
from django.shortcuts import render, redirect
# from mr.proc import realisasi_PRA

# Create your views here.
def home_view(request):
    try:
        template = "home/template/home.html"
        context = {}
        context["daftar_kasus"] = getKasus()
        context["title"] = "KMS-OC"
        if not request.user.is_authenticated:
            return redirect("/pegawai/login")
        return render(request, template, context)
    except Exception as e:
        print("error: ", e)
        return redirect("/home/404")

def error_view(request):
    template = "template/404.html"
    context = {}
    context["title"] = "Error Page"

    if not request.user.is_authenticated:
        return redirect("/pegawai/login")
    return render(request, template, context)