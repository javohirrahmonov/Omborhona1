from django.shortcuts import render , redirect
from .models import *
from django.contrib.auth import authenticate,login , logout
from django.contrib import messages
from asosiy.models import *

def login_view(request):
    if request.method == 'POST':
        user = authenticate(
            username = request.POST['l'],
            password = request.POST['p']
        )
        if user is None:
            messages.error(request,'Login yoki parolda xatolik bor')
            return redirect('login')
        login(request,user)
        return redirect("/bolimlar/")
    return render(request,'home.html')

def logout_view(request):
    logout(request)
    return redirect("/")
