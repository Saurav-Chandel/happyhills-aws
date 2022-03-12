from rest_framework import serializers
from django.db.models import Avg
from review.models import Review
from .models import *


class PackageSerializer(serializers.ModelSerializer):
    rating = serializers.SerializerMethodField(method_name='get_review')

    class Meta(object):
        model = Package
        fields = "__all__"

    def get_review(self,obj):
        queryset=Review.objects.filter(package=obj.id).aggregate(Avg('rating'))
        return queryset


class CreatePackageSerializer(serializers.ModelSerializer):
    # images = serializers.ListField(
    #                    child=serializers.FileField( max_length=100000,
    #                                      allow_empty_file=False,
    #                                      use_url=False )
    #                             ) 
    class Meta(object):
        model = Package
        fields = "__all__"

    # def create(self, validated_data):
    #     package=Package.objects.latest('created_at')
    #     image=validated_data.pop('images')
    #     for img in images:
    #         package=Package.objects.create(image=img,package=package,**validated_data)
    #     return package    



# class FileListSerializer ( serializers.Serializer ) :
#     images = serializers.ListField(
#                        child=serializers.FileField( max_length=100000,
#                                          allow_empty_file=False,
#                                          use_url=False )
#                                 )
#     def create(self, validated_data):
#         package=Package.objects.latest('created_at')
#         image=validated_data.pop('images')
#         for img in images:
#             package=Package.objects.create(image=img,package=package,**validated_data)
#         return package

  
        