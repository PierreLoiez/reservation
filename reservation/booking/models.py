from django.db import models
from django.contrib.auth import models as m

# Create your models here.

class Gare(models.Model):
    nom = models.CharField(max_length = 100, primary_key=True)


class Trajet(models.Model):
    id = models.IntegerField(primary_key=True)
    gareDepart = models.ForeignKey(Gare, on_delete=models.CASCADE, related_name="partantDe")
    gareArrivee = models.ForeignKey(Gare, on_delete=models.CASCADE, related_name="arrivantA")
    DHDepart = models.DateTimeField()
    DHArrivee = models.DateTimeField()

class Passager(models.Model):
    id = models.IntegerField(primary_key=True)
    nom = models.CharField(max_length=30)
    prenom = models.CharField(max_length=30)
    dateDeNaissance = models.DateField()

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


