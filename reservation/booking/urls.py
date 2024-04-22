from . import views
from django.urls import include, path

app_name = "booking"
urlpatterns = [
    path("trajets/", views.Trajets, name="Trajets")
]