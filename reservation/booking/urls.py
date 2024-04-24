from . import views
from django.urls import include, path

app_name = "booking"
urlpatterns = [
    path("trajets/", views.Trajets, name="Trajets"),
    path("reservations/", views.Reservations, name="Reservations"),
    path("reservations/<int:pk>/", views.ReservationDeet, name="Reservation")
    
]