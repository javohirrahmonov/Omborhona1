
from django.shortcuts import render , redirect
from .models import *
from django.contrib.auth import authenticate,login , logout
from django.contrib import messages
from userapp.models import Ombor
from asosiy.models import Mijoz , Mahsulot
from .models import *

def statistikalar(request):
    if request.user.is_authenticated:
        soz = request.GET.get('soz')
        stats =  Statistika.objects.filter(ombor__user=request.user)
        if soz:
            stats = stats.filter(mahsulot__nom=soz)|stats.filter(mijoz__ism=soz)
        if request.method == 'POST':
            Statistika.objects.create(
                mahsulot = Mahsulot.objects.get(id=request.POST['m']),
                mijoz = Mijoz.objects.get(id = request.POST['c']),
                sana = request.POST['s'],
                miqdor = request.POST['miq'],
                umumiy_summa = request.POST['u_s'],
                tolandi = request.POST['t'],
                nasiy = request.POST['n'],
                ombor=Ombor.objects.get(user=request.user)
        )
            return redirect('statistikalar')
        content = {
            'statistikalar': stats,
            'mijozlar': Mijoz.objects.filter(ombor__user=request.user),
            'mahsulotlar': Mahsulot.objects.filter(ombor__user=request.user)
        }
        return render(request,'stats.html',content)
