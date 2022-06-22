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

class GetAllState(APIView):
    """
    Get All State
    """
    permission_classes = [permissions.AllowAny]
    # authentication_classes = [authentication.JWTAuthentication]

    @csrf_exempt
    def get(self, request):
        try:
            state=State.objects.all()
            serializer=StateSerializer(state,many=True)
            return ResponseOk(
                {
                    "data": serializer.data,
                    "code": status.HTTP_200_OK,
                    "message": "State list",
                }
            )
        except:
            return ResponseBadRequest(
                {
                    "data": serializer.errors,
                    "code": status.HTTP_400_BAD_REQUEST,
                    "message": "State Does Not Exist",
                }
            )




class CreateState(APIView):
    """
    Create State
    """

    permission_classes = [permissions.AllowAny]
    # authentication_classes = [authentication.JWTAuthentication]
    parser_classes = (FormParser, MultiPartParser)


    @swagger_auto_schema(
        operation_description="create State",
        request_body=StateSerializer,
    )
    @csrf_exempt
    def post(self, request):
        serializer = StateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return ResponseOk(
                {
                    "data": serializer.data,
                    "code": status.HTTP_200_OK,
                    "message": "State created succesfully",
                }
            )
            return ResponseBadRequest(
                {
                    "data": serializer.errors,
                    "code": status.HTTP_400_BAD_REQUEST,
                    "message": "State is not valid",
                }
            )



class GetState(APIView):
    """
    Get State by pk
    """
    
    permission_classes = [permissions.AllowAny]
    # authentication_classes = [authentication.JWTAuthentication]

    csrf_exempt

    def get_object(self, pk):
        try:
            return State.objects.get(pk=pk)
        except State.DoesNotExist:
            raise ResponseNotFound()

    def get(self, request, pk):
        try:
            state = self.get_object(pk)
            serializer = StateSerializer(state)
            return ResponseOk(
                {
                    "data": serializer.data,
                    "code": status.HTTP_200_OK,
                    "message": "get State successfully",
                }
            )
        except:
            return ResponseBadRequest(
                {
                    "data": None,
                    "code": status.HTTP_400_BAD_REQUEST,
                    "message": "State Does Not Exist",
                }
            )




class UpdateState(APIView):
    """
    Update State
    """

    permission_classes = [permissions.AllowAny]
    # authentication_classes = [authentication.JWTAuthentication]
    parser_classes = (FormParser, MultiPartParser)


    def get_object(self, pk):
        try:
            return State.objects.get(pk=pk)
        except State.DoesNotExist:
            raise ResponseNotFound()

    @swagger_auto_schema(
        operation_description="create State",
        request_body=StateSerializer,
    )
    @csrf_exempt
    def put(self, request, pk):
        try:
            state = self.get_object(pk)
            serializer = StateSerializer(state, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return ResponseOk(
                    {
                        "data": serializer.data,
                        "code": status.HTTP_200_OK,
                        "message": "State updated successfully",
                    }
                )
            else:
                return ResponseBadRequest(
                    {
                        "data": serializer.errors,
                        "code": status.HTTP_400_BAD_REQUEST,
                        "message": "State Not valid",
                    }
                )
        except:
            return ResponseBadRequest(
                {
                    "data": None,
                    "code": status.HTTP_400_BAD_REQUEST,
                    "message": "State Does Not Exist",
                }
            )



class DeleteState(APIView):
    """
    Delete State
    """

    permission_classes = [permissions.AllowAny]
    # authentication_classes = [authentication.JWTAuthentication]

    @csrf_exempt
    def get_object(self, pk):
        try:
            return State.objects.get(pk=pk)
        except State.DoesNotExist:
            raise ResponseNotFound()

    def delete(self, request, pk):
        try:
            state = self.get_object(pk)
            state.delete()
            return ResponseOk(
                {
                    "data": None,
                    "code": status.HTTP_200_OK,
                    "message": "State deleted Successfully",
                }
            )
        except:
            return ResponseBadRequest(
                {
                    "data": None,
                    "code": status.HTTP_400_BAD_REQUEST,
                    "message": "State Does Not Exist",
                }
            )


class GetAllDistrict(APIView):
    """
    Get All District
    """
    permission_classes = [permissions.AllowAny]
    # authentication_classes = [authentication.JWTAuthentication]

    @csrf_exempt
    def get(self, request):
        try:
            district=District.objects.all()
            serializer=DistrictSerializer(district,many=True)
            return ResponseOk(
                {
                    "data": serializer.data,
                    "code": status.HTTP_200_OK,
                    "message": "District list",
                }
            )
        except:
            return ResponseBadRequest(
                {
                    "data": serializer.errors,
                    "code": status.HTTP_400_BAD_REQUEST,
                    "message": "District Does Not Exist",
                }
            )




class CreateDistrict(APIView):
    """
    Create District
    """

    permission_classes = [permissions.AllowAny]
    # authentication_classes = [authentication.JWTAuthentication]
    parser_classes = (FormParser, MultiPartParser)


    @swagger_auto_schema(
        operation_description="create District",
        request_body=DistrictSerializer,
    )
    @csrf_exempt
    def post(self, request):
        serializer = DistrictSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return ResponseOk(
                {
                    "data": serializer.data,
                    "code": status.HTTP_200_OK,
                    "message": "District created succesfully",
                }
            )
            return ResponseBadRequest(
                {
                    "data": serializer.errors,
                    "code": status.HTTP_400_BAD_REQUEST,
                    "message": "District is not valid",
                }
            )



class GetDistrict(APIView):
    """
    Get District by pk
    """
    
    permission_classes = [permissions.AllowAny]
    # authentication_classes = [authentication.JWTAuthentication]

    csrf_exempt
    def get_object(self, pk):
        try:
            return D.objects.get(pk=pk)
        except D.DoesNotExist:
            raise ResponseNotFound()

    def get(self, request, pk):
        try:
            district = self.get_object(pk)
            serializer = DistrictSerializer(district)
            return ResponseOk(
                {
                    "data": serializer.data,
                    "code": status.HTTP_200_OK,
                    "message": "get District successfully",
                }
            )
        except:
            return ResponseBadRequest(
                {
                    "data": None,
                    "code": status.HTTP_400_BAD_REQUEST,
                    "message": "District Does Not Exist",
                }
            )




class UpdateDistrict(APIView):
    """
    Update District
    """

    permission_classes = [permissions.AllowAny]
    # authentication_classes = [authentication.JWTAuthentication]
    parser_classes = (FormParser, MultiPartParser)


    def get_object(self, pk):
        try:
            return D.objects.get(pk=pk)
        except D.DoesNotExist:
            raise ResponseNotFound()

    @swagger_auto_schema(
        operation_description="update District",
        request_body=DistrictSerializer,
    )
    @csrf_exempt
    def put(self, request, pk):
        try:
            district = self.get_object(pk)
            serializer = DistrictSerializer(district, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return ResponseOk(
                    {
                        "data": serializer.data,
                        "code": status.HTTP_200_OK,
                        "message": "District updated successfully",
                    }
                )
            else:
                return ResponseBadRequest(
                    {
                        "data": serializer.errors,
                        "code": status.HTTP_400_BAD_REQUEST,
                        "message": "District Not valid",
                    }
                )
        except:
            return ResponseBadRequest(
                {
                    "data": None,
                    "code": status.HTTP_400_BAD_REQUEST,
                    "message": "District Does Not Exist",
                }
            )



class DeleteDistrict(APIView):
    """
    Delete District
    """

    permission_classes = [permissions.AllowAny]
    # authentication_classes = [authentication.JWTAuthentication]

    @csrf_exempt
    def get_object(self, pk):
        try:
            return D.objects.get(pk=pk)
        except D.DoesNotExist:
            raise ResponseNotFound()

    def delete(self, request, pk):
        try:
            district = self.get_object(pk)
            district.delete()
            return ResponseOk(
                {
                    "data": None,
                    "code": status.HTTP_200_OK,
                    "message": "district deleted Successfully",
                }
            )
        except:
            return ResponseBadRequest(
                {
                    "data": None,
                    "code": status.HTTP_400_BAD_REQUEST,
                    "message": "district Does Not Exist",
                }
            )


class GetAllDestination(APIView):
    """
    Get All Destination
    """
    permission_classes = [permissions.AllowAny]
    # authentication_classes = [authentication.JWTAuthentication]

    @csrf_exempt
    def get(self, request):
        try:
            destination=Destination.objects.all()
            serializer=GetDestinationSerializer(destination,many=True)
            return ResponseOk(
                {
                    "data": serializer.data,
                    "code": status.HTTP_200_OK,
                    "message": "Destination list",
                }
            )
        except:
            return ResponseBadRequest(
                {
                    "data": serializer.errors,
                    "code": status.HTTP_400_BAD_REQUEST,
                    "message": "Destination Does Not Exist",
                }
            )




class CreateDestination(APIView):
    """
    Create Destination
    """

    permission_classes = [permissions.AllowAny]
    # authentication_classes = [authentication.JWTAuthentication]
    parser_classes = (FormParser, MultiPartParser)


    @swagger_auto_schema(
        operation_description="create Destination",
        request_body=DestinationSerializer,
    )
    @csrf_exempt
    def post(self, request):
        serializer = DestinationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return ResponseOk(
                {
                    "data": serializer.data,
                    "code": status.HTTP_200_OK,
                    "message": "Destination created succesfully",
                }
            )
            return ResponseBadRequest(
                {
                    "data": serializer.errors,
                    "code": status.HTTP_400_BAD_REQUEST,
                    "message": "Destination is not valid",
                }
            )



class GetDestination(APIView):
    """
    Get Destination by pk
    """
    
    permission_classes = [permissions.AllowAny]
    # authentication_classes = [authentication.JWTAuthentication]

    csrf_exempt
    def get_object(self, pk):
        try:
            return Destination.objects.get(pk=pk)
        except Destination.DoesNotExist:
            raise ResponseNotFound()

    def get(self, request, pk):
        try:
            destination = self.get_object(pk)
            serializer = GetDestinationSerializer(destination)
            return ResponseOk(
                {
                    "data": serializer.data,
                    "code": status.HTTP_200_OK,
                    "message": "get Destination successfully",
                }
            )
        except:
            return ResponseBadRequest(
                {
                    "data": None,
                    "code": status.HTTP_400_BAD_REQUEST,
                    "message": "Destination Does Not Exist",
                }
            )




class UpdateDestination(APIView):
    """
    Update Destination
    """

    permission_classes = [permissions.AllowAny]
    # authentication_classes = [authentication.JWTAuthentication]
    parser_classes = (FormParser, MultiPartParser)


    def get_object(self, pk):
        try:
            return Destination.objects.get(pk=pk)
        except Destination.DoesNotExist:
            raise ResponseNotFound()

    @swagger_auto_schema(
        operation_description="update Destination",
        request_body=DestinationSerializer,
    )
    @csrf_exempt
    def put(self, request, pk):
        try:
            destination = self.get_object(pk)
            serializer = DestinationSerializer(destination, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return ResponseOk(
                    {
                        "data": serializer.data,
                        "code": status.HTTP_200_OK,
                        "message": "Destination updated successfully",
                    }
                )
            else:
                return ResponseBadRequest(
                    {
                        "data": serializer.errors,
                        "code": status.HTTP_400_BAD_REQUEST,
                        "message": "Destination Not valid",
                    }
                )
        except:
            return ResponseBadRequest(
                {
                    "data": None,
                    "code": status.HTTP_400_BAD_REQUEST,
                    "message": "Destination Does Not Exist",
                }
            )



class DeleteDestination(APIView):
    """
    Delete Destination
    """

    permission_classes = [permissions.AllowAny]
    # authentication_classes = [authentication.JWTAuthentication]

    @csrf_exempt
    def get_object(self, pk):
        try:
            return Destination.objects.get(pk=pk)
        except Destination.DoesNotExist:
            raise ResponseNotFound()

    def delete(self, request, pk):
        try:
            destination = self.get_object(pk)
            destination.delete()
            return ResponseOk(
                {
                    "data": None,
                    "code": status.HTTP_200_OK,
                    "message": "Destination deleted Successfully",
                }
            )
        except:
            return ResponseBadRequest(
                {
                    "data": None,
                    "code": status.HTTP_400_BAD_REQUEST,
                    "message": "Destination Does Not Exist",
                }
            )

