from django import forms
from .models import Passager, Reservation, Client

class ResForm(forms.ModelForm):
    def __init__(self, request, *args, **kwargs):
        super(ResForm, self).__init__(*args, **kwargs)
        self.fields['passager'].queryset = Passager.objects.filter(client=Client.objects.get(user=request.user))
        
    class Meta:
        model = Reservation
        fields = ('trajet', 'passager', 'numeroPlace')

class PassagerForm(forms.ModelForm):
    
    class Meta:
        model = Passager
        fields = ('nom', 'prenom', 'dateDeNaissance')

