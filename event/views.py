from django.shortcuts import render
from rest_framework import viewsets

from event.models import EventReservation, Reservation, event
from .serializers import eventSerializer,EventReservationSerializer,ReservationSerializer


class eventViewSet(viewsets.ModelViewSet):
    queryset = event.objects.all()
    serializer_class = eventSerializer
    
class ReservationViewset(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    
class EventReservationViewSet(viewsets.ModelViewSet):
    queryset = EventReservation.objects.all()
    serializer_class = EventReservationSerializer