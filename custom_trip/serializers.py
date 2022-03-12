from rest_framework import serializers
from .models import *
from package.serializers import *


class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model=State
        fields="__all__"


class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model=District
        fields="__all__"

class GetDestinationSerializer(serializers.ModelSerializer):
    # district=DistrictSerializer(read_only=True)
    # package=PackageSerializer(read_only=True)
    class Meta:
        model=Destination
        fields="__all__"      

class DestinationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Destination
        fields="__all__"             