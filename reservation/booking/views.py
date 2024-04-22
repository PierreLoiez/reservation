
from .models import Trajet, Client, Passager
from django.shortcuts import render


# Create your views here.
def Trajets(request):
    context = {"trajets" : Trajet.objects.order_by("gareDepart")}
    template = "booking/trajets.html"
    return render(request, template, context)
