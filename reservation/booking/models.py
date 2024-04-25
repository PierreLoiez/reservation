from django.db import models
from django.contrib.auth import models as m

import random
# Create your models here.

class Gare(models.Model):
    nom = models.CharField(max_length = 100, primary_key=True)
    def __str__(self):
        return self.nom

class Trajet(models.Model):
    id = models.IntegerField(primary_key=True)
    gareDepart = models.ForeignKey(Gare, on_delete=models.CASCADE, related_name="partantDe")
    gareArrivee = models.ForeignKey(Gare, on_delete=models.CASCADE, related_name="arrivantA")
    DHDepart = models.DateTimeField()
    DHArrivee = models.DateTimeField()
    
    def __str__(self):
        return self.gareDepart.nom + " -- " + self.gareArrivee.nom



class Client(models.Model):
    
    prenom = models.CharField(max_length=30)
    nom = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    addresse = models.CharField(max_length=100)
    telephone = models.BigIntegerField(default=0)
    user = models.OneToOneField(
        m.User(first_name = prenom, last_name = nom, email = email),
        on_delete=models.CASCADE, 
        
        )
    def __str__(self):
        return self.nom.upper() + " " + self.prenom.title()

    
class Passager(models.Model):
    id = models.IntegerField(primary_key=True)
    nom = models.CharField(max_length=30)
    prenom = models.CharField(max_length=30)
    dateDeNaissance = models.DateField()
    client = models.ForeignKey(Client, on_delete=models.CASCADE, default=2)
    def __str__(self):
        return self.nom.upper() + " " + self.prenom.title()

    
class Reservation(models.Model):
    dateResa = models.DateField(auto_now=True)
    numeroResa = models.IntegerField(primary_key=True)
    numeroPlace = models.IntegerField()
    trajet = models.ForeignKey(Trajet, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    passager = models.ForeignKey(Passager, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.trajet) + " avec "  + str(self.passager) + " place " + str(self.numeroPlace)
    

