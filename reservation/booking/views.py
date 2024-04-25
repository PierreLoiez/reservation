
from .models import Trajet, Client, Passager, Reservation
from django.shortcuts import render, redirect
from django.http import Http404
from .forms import ResForm, PassagerForm
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


def EditRes(request, id=None):
    template = "booking/edit_reservation.html"
    
    
    if request.method == 'POST':
        input_form = ResForm(request, request.POST)
        
        
        if id != None:
            reservation = input_form.save(commit=False)
            resa = Reservation.objects.get(numeroResa=id)
            resa.passager = reservation.passager
            resa.trajet = reservation.trajet
            resa.numeroPlace = reservation.numeroPlace
            reservation.delete()
            resa.save()
            url = '/booking/reservations/' + str(id)
            
        else:
            reservation = input_form.save(commit=False)
            reservation.client = Client.objects.get(user=request.user)
            reservation.numeroResa = len(Reservation.objects.order_by('numeroResa'))
            reservation.save()
            url = '/booking/reservations/'+str(reservation.numeroResa)
        return redirect(url)
            
    else:
        if id != None:
            resa = Reservation.objects.get(numeroResa=id)
            input_form = ResForm(request, initial={'passager':resa.passager, 'trajet':resa.trajet, 'numeroPlace':resa.numeroPlace, })

        else:
            input_form = ResForm(request)
        
        
            
    
    context = {"form" : input_form} 
    return render(request, template, context)

def Homepage(request):
    template = "booking/homepage.html"
    return render(request, template)

def CreerPass(request):
    template = "booking/create_pass.html"
        
    if request.method == 'POST':
        input_form = PassagerForm(request.POST)
        
        passager = input_form.save(commit=False)
        passager.client = Client.objects.get(user=request.user)
        passager.save()
        return redirect('/booking/nouvelle_reservation')
    else:
        input_form = PassagerForm()
    context = {"form" : input_form} 
    return render(request, template, context)
   

    