from django.shortcuts import render, HttpResponse
from hello.models import Produkt, Osoba

# widoki zawsze muszą mieć parametr `request` i muszą zwracać obiekt `HttpResponse`

# Create your views here.
def hello_view(request):
    return HttpResponse("Witam!")

def czesc(request, imie):
    return HttpResponse(f"Cześć, {imie}!")

def oblicz(request, dzialanie, a, b):
    a = int(a)
    b = int(b)
    if dzialanie == 'dod':
        return HttpResponse(f"{a} + {b} = {a + b}")
    elif dzialanie == "ode":
        return HttpResponse(f"{a} - {b} = {a - b}")
    else:
        return HttpResponse("Błędne działanie!")


def lista_produktow(request):
    lista = Produkt.objects.filter(dostepny=True)  # pobieramy tylko produkty, dla których dostepny=True
    # lista = Produkt.objects.all()  # pobieramy wszystkie produkty z bazy
    return render(request, "lista_produktow.html", context={"produkty": lista})