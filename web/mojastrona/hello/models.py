from django.db import models

# Create your models here.
class Osoba(models.Model):
    imie = models.CharField(max_length=30)
    nazwisko = models.CharField(max_length=30)


class Produkt(models.Model):
    nazwa = models.CharField(max_length=20)
    opis = models.TextField()
    cena = models.DecimalField(max_digits=5, decimal_places=2)
    dostepny = models.BooleanField()