from django.shortcuts import render,redirect
from .models import UserRegister
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request,'home.html')
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if UserRegister.objects.filter(username=username).exists():
            return render(request, "register.html", {
                "error": "Username already taken!"
            })

        UserRegister.objects.create(username=username,email=email,password=password) 
        return redirect(login)   
    return render(request,'register.html')
def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        try:
            UserRegister.objects.get(email=email,password=password)
            return HttpResponse("Login Success")
        except UserRegister.DoesNotExist:
            return HttpResponse("Invalid Login credentials")
    return render(request,'login.html')

