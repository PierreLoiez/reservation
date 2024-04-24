from django import forms
from .models import Passager, Reservation

class ResForm(forms.ModelForm):
    
    class Meta:
        model = Reservation
        fields = ('trajet', 'passager', 'numeroPlace')

class PassagerForm(forms.ModelForm):
    
    class Meta:
        model = Passager
        fields = ('nom', 'prenom', 'dateDeNaissance')

