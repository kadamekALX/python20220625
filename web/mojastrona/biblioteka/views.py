from django.shortcuts import render, get_object_or_404

# Create your views here.
from biblioteka.models import Autor, Ksiazka


def lista_autorow(request):
    lista = Autor.objects.all()
    return render(request, "lista_autorow.html", {"autorzy": lista})


def szczegoly_autora(request, id):
    autor = get_object_or_404(Autor, id=id)
    ksiazki = Ksiazka.objects.filter(autor__id=id)  # wszystkie ksiazki, ktorych autor ma to samo id, co autor, ktorego pobralismy z bazy
    return render(request, "szczegoly_autora.html", {"autor": autor, "ksiazki": ksiazki})