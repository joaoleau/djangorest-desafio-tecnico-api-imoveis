from rest_framework import serializers, validators
from .models import Immobile, Advertisement, Reservation


class immobileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Immobile
        fields = "__all__"

class AdvertisementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertisement
        fields = "__all__"

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = "__all__"
    
    def create(self, validated_data):
        if validated_data.get("check_in") > validated_data.get("check_out"):
            raise validators.ValidationError("Data de check-in nao pode ser posterior a de check-out")
        
        return super(ReservationSerializer, self).create(validated_data)