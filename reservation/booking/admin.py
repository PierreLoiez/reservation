from django.contrib import admin
from .models import Gare, Trajet, Passager, Client, Reservation
# Register your models here.
admin.site.register(Gare)
admin.site.register(Reservation)
admin.site.register(Trajet)
admin.site.register(Passager)
admin.site.register(Client)
