from rest_framework import serializers
from .models import *
# from user.serializers import UserSerializer,MediaSerializer




class ReviewSerializer(serializers.ModelSerializer):
   
    class Meta(object):
        model = Review
        fields = "__all__"