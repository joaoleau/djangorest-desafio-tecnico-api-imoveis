from django.shortcuts import render
from rest_framework import generics

from .models import Immobile, Advertisement, Reservation
from .serializers import immobileSerializer, AdvertisementSerializer, ReservationSerializer

class ImmobileList(generics.ListCreateAPIView):
    queryset = Immobile.objects.all()
    serializer_class = immobileSerializer

class ImmobileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Immobile.objects.all()
    serializer_class = immobileSerializer


class AdvertisementList(generics.ListCreateAPIView):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer

class AdvertisementDetail(generics.RetrieveUpdateAPIView):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer


class ReservationList(generics.ListCreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

class ReservationtDetail(generics.RetrieveDestroyAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer