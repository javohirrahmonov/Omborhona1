from django.db import models
from userapp.models import Ombor
from asosiy.models import Mahsulot , Mijoz

class Statistika(models.Model):
    mahsulot = models.ForeignKey(Mahsulot, on_delete= models.SET_NULL, null= True)
    mijoz = models.ForeignKey(Mijoz, on_delete= models.SET_NULL, null= True)
    ombor = models.ForeignKey(Ombor, on_delete= models.SET_NULL, null= True)
    sana = models.DateTimeField(auto_now_add= True)
    miqdor = models.PositiveSmallIntegerField()
    umumiy_summa = models.PositiveIntegerField()
    tolandi = models.PositiveIntegerField()
    nasiy = models.PositiveIntegerField()

    def save(self,*args,**kwargs):
        self.umumiy_summa = int(self.miqdor) * int(self.maxsulot.narx)
        self.nasiya = self.umumiy_summa - int(self.tolandi)
        super