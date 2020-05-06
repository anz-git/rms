from django.shortcuts import render



# Create your views here.
def login(request):
    return render(request,"login_app/login.html")
def add(request):
    return render(request,"login_app/add.html")
def main(request):
    return render(request,"login_app/main.html")
def signup(request):
    return render(request,"login_app/signup.html")    