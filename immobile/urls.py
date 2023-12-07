from django.urls import path
from .views import (
ImmobileList,
ImmobileDetail, 
AdvertisementList,
AdvertisementDetail,
ReservationList,
ReservationtDetail
)

urlpatterns = [
    path("immobiles/", ImmobileList.as_view(),name="immobile-list"),
    path("immobiles/<int:pk>/", ImmobileDetail.as_view(), name="immobile-detail"),

    path("advertisement/", AdvertisementList.as_view(),name="advertisement-list"),
    path("advertisement/<int:pk>/", AdvertisementDetail.as_view(), name="advertisement-detail"),

    path("reservation/", ReservationList.as_view(),name="reservation-list"),
    path("reservation/<int:pk>/", ReservationtDetail.as_view(), name="reservation-detail"),
]
