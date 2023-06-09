from django.shortcuts import render , redirect
from .models import *
from django.contrib.auth import authenticate,login , logout
from django.contrib import messages
from userapp.models import Ombor
from statsapp.models import Statistika


def bolimlar(request):
    if request.user.is_authenticated:
        return render(request,'bulimlar.html')
    return redirect('ligin')


def mahsulotlar(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            Mahsulot.objects.create(
                nom = request.POST['n'],
                brend = request.POST['b'],
                narx = request.POST['na'],
                miqdor = request.POST['m'],
                olchov = request.POST['o'],
                sana = request.POST['s'],
                ombor = Ombor.objects.get(user = request.user)
        )
            return redirect('/mahsulotlar/')
        content = {
            'mahsulotlar': Mahsulot.objects.filter(ombor__user=request.user)
        }
        return render(request,'products.html',content)

def mahsulot_ochir(request,pk):
    if request.user.is_authenticated:
        Mahsulot.objects.filter(id=pk ,ombor__user=request.user).delete()
        return redirect('mahsulotlar')
    return redirect('login')


def product_edit(request,son):
    if request.method=='POST':
        Mahsulot.objects.filter(id=son).update(
        nom = request.POST.get('n'),
        brend =request.POST.get('b'),
        narx =request.POST.get('na'),
        miqdor = request.POST['m'],
        olchov = request.POST['o'],
        sana = request.POST['s'],
        )
        return redirect('mahsulotlar')
    content = {
        'product': Mahsulot.objects.get(id=son)
    }
    return render(request,'product_update.html',content)

def clientlar(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            Mijoz.objects.create(
                ism = request.POST['i'],
                nom = request.POST['n'],
                tel =request.POST['t'],
                manzil = request.POST['m'],
                qarz = request.POST['q'],
                ombor = Ombor.objects.get(user=request.user)
            )
            return redirect("clientlar")
        content = {
            'clientlar': Mijoz.objects.filter(ombor__user=request.user)
        }
        return render(request,'clients.html',content)

def client_ochir(request,pk):
    if request.user.is_authenticated:
        Mijoz.objects.filter(id=pk ,ombor__user=request.user).delete()
        return redirect('clientlar')
    return redirect('login')

def mijoz_edit(request,son):
    if request.method=='POST':
        Mijoz.objects.filter(id=son).update(
        ism = request.POST.get('i'),
        nom =request.POST.get('n'),
        tel =request.POST.get('t'),
        qarz = request.POST['q'],
        manzil = request.POST['m'],
        )
        return redirect('clientlar')
    content = {
        'client': Mijoz.objects.get(id=son)
    }
    return render(request,'client_update.html',content)


