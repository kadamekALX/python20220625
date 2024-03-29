"""mojastrona URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from hello.views import hello_view, czesc, oblicz, lista_produktow, szczegoly_produktu

from biblioteka.views import lista_autorow, szczegoly_autora

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello_view),
    path('czesc/<imie>/', czesc),
    path('dzialanie/<dzialanie>/<a>/<b>/', oblicz),
    path('produkty/', lista_produktow, name="lista_produktow"),
    path('produkt/<int:id>/', szczegoly_produktu, name="szczegoly_produktu"),
    path('biblioteka/autorzy/', lista_autorow, name="lista_autorow"),
    path('biblioteka/autor/<int:id>/', szczegoly_autora, name="szczegoly_autora"),
]
