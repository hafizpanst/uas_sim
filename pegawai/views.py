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