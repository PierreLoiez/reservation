from . import views
from django.urls import include, path

app_name = "booking"
urlpatterns = [
    path("trajets/", views.Trajets, name="Trajets"),
    path("reservations/", views.Reservations, name="Reservations"),
    path("reservations/<int:pk>/", views.ReservationDeet, name="Reservation"),
    path("nouvelle_reservation/", views.EditRes, name="NouvelleResa"),
    path("modif_reservation/<int:id>", views.EditRes, name="ModifResa"),
    path("", views.Homepage, name="Homepage"), 
    path("create_pass/", views.CreerPass, name="CreerPass")
    
]