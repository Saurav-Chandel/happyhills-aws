from django.shortcuts import render
from rest_framework import permissions, status
from rest_framework_simplejwt import authentication
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from django.views.decorators.csrf import csrf_exempt
from drf_yasg import openapi
from app.response import ResponseBadRequest, ResponseNotFound, ResponseOk
from rest_framework.parsers import FormParser, MultiPartParser
from .models import *
from .serializers import *

# Create your views here.



class GetAllPackage(APIView):
    """
    Get All Package
    """
    # permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.JWTAuthentication]

    @csrf_exempt
    def get(self, request):
        try:
            package=Package.objects.all()
            serializer=PackageSerializer(package,many=True)
            return ResponseOk(
                {
                    "data": serializer.data,
                    "code": status.HTTP_200_OK,
                    "message": "Package list",
                }
            )
        except:
            return ResponseBadRequest(
                {
                    "data": serializer.errors,
                    "code": status.HTTP_400_BAD_REQUEST,
                    "message": "Package Does Not Exist",
                }
            )




class CreatePackage(APIView):
    """
    Create Package
    """

    # permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.JWTAuthentication]
    parser_classes = (FormParser, MultiPartParser)


    @swagger_auto_schema(
        operation_description="create Package",
        request_body=CreatePackageSerializer,
    )
    @csrf_exempt
    def post(self, request):
        serializer = CreatePackageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return ResponseOk(
                {
                    "data": serializer.data,
                    "code": status.HTTP_200_OK,
                    "message": "Package created succesfully",
                }
            )
            return ResponseBadRequest(
                {
                    "data": serializer.errors,
                    "code": status.HTTP_400_BAD_REQUEST,
                    "message": "Package is not valid",
                }
            )



class GetPackage(APIView):
    """
    Get Package by pk
    """
    
    # permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.JWTAuthentication]

    csrf_exempt

    def get_object(self, pk):
        try:
            return Package.objects.get(pk=pk)
        except Package.DoesNotExist:
            raise ResponseNotFound()

    def get(self, request, pk):
        try:
            package = self.get_object(pk)
            serializer = PackageSerializer(package)
            return ResponseOk(
                {
                    "data": serializer.data,
                    "code": status.HTTP_200_OK,
                    "message": "get Package successfully",
                }
            )
        except:
            return ResponseBadRequest(
                {
                    "data": None,
                    "code": status.HTTP_400_BAD_REQUEST,
                    "message": "Package Does Not Exist",
                }
            )




class UpdatePackage(APIView):
    """
    Update Package
    """

    # permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.JWTAuthentication]
    parser_classes = (FormParser, MultiPartParser)


    def get_object(self, pk):
        try:
            return Package.objects.get(pk=pk)
        except Package.DoesNotExist:
            raise ResponseNotFound()

    @swagger_auto_schema(
        operation_description="create Package",
        request_body=PackageSerializer,
    )
    @csrf_exempt
    def put(self, request, pk):
        try:
            package = self.get_object(pk)
            serializer = CreatePackageSerializer(package, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return ResponseOk(
                    {
                        "data": serializer.data,
                        "code": status.HTTP_200_OK,
                        "message": "Package updated successfully",
                    }
                )
            else:
                return ResponseBadRequest(
                    {
                        "data": serializer.errors,
                        "code": status.HTTP_400_BAD_REQUEST,
                        "message": "Package Not valid",
                    }
                )
        except:
            return ResponseBadRequest(
                {
                    "data": None,
                    "code": status.HTTP_400_BAD_REQUEST,
                    "message": "Package Does Not Exist",
                }
            )



class DeletePackage(APIView):
    """
    Delete Package
    """

    # permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.JWTAuthentication]

    @csrf_exempt
    def get_object(self, pk):
        try:
            return Package.objects.get(pk=pk)
        except Package.DoesNotExist:
            raise ResponseNotFound()

    def delete(self, request, pk):
        try:
            package = self.get_object(pk)
            package.delete()
            return ResponseOk(
                {
                    "data": None,
                    "code": status.HTTP_200_OK,
                    "message": "Package deleted Successfully",
                }
            )
        except:
            return ResponseBadRequest(
                {
                    "data": None,
                    "code": status.HTTP_400_BAD_REQUEST,
                    "message": "Package Does Not Exist",
                }
            )


