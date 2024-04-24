
from .models import Trajet, Client, Passager, Reservation
from django.shortcuts import render
from django.http import Http404

# Create your views here.
def Trajets(request):
    context = {"trajets" : Trajet.objects.order_by("gareDepart")}
    template = "booking/trajets.html"
    return render(request, template, context)

def Reservations(request):
    context = {"resas" : Reservation.objects.filter(client=Client.objects.get(user=request.user)).order_by("numeroResa")}
    template = "booking/reservations.html"
    return render(request, template, context)

def ReservationDeet(request, pk):
    try:
        resa = Reservation.objects.get(pk=pk)
    except:
        raise Http404("Reservation does not exist")
    template = "booking/reservation.html"
    return render(request, template, {"resa" : resa})