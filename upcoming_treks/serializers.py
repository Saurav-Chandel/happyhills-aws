from rest_framework import serializers
from .models import *


class UpcomingTreksSerializer(serializers.ModelSerializer):
    class Meta:
        model=Upcoming_Treks
        fields="__all__"

class UpcomingRoadTripsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Upcoming_Road_Trips
        fields="__all__"        