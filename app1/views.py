from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def newlyassignleads(request):
    return render(request,'newlyassignedleads.html') 

def currentleads(request):
    return render(request,'currentleads.html')

def previousleads(request):
    return render(request,'previousleads.html')

def login(request):
    return render(request,'login.html')

def register(request):
    return render(request,'register.html') 
def dashboard(request):
    return render(request,'dashboard.html')       