from django.shortcuts import render



# Create your views here.
def login(request):
    return render(request,"login.html")
def add(request):
    return render(request,"add.html")
def main(request):
    return render(request,"main.html")
def signup(request):
    return render(request,"signup.html")    