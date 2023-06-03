from django.db import models
from userapp.models import Ombor

class Mahsulot(models.Model):
    nom = models.CharField(max_length=70)
    brend = models.CharField(max_length=70)
    narx = models.IntegerField()
    miqdor = models.PositiveSmallIntegerField()
    olchov = models.CharField(max_length=30,choices = (("dona","dona"),("kg","kg"),("qop","qop"),("blok","blok"),("litr","litr")))
    sana = models.DateField(max_length=70)
    ombor = models.ForeignKey(Ombor, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.nom}, {self.brend}"


class Mijoz(models.Model):
    ism = models.CharField(max_length=70)
    nom = models.CharField(max_length=70)
    tel = models.CharField(max_length=70)
    manzil = models.CharField(max_length=70)
    qarz = models.IntegerField()
    ombor = models.ForeignKey(Ombor , on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.ism}, {self.nom}"