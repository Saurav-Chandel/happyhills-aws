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
class GetAllUpcomingTreks(APIView):
    """
    Get All Upcoming_Treks
    """
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.JWTAuthentication]

    @csrf_exempt
    def get(self, request):
        try:
            upcoming_treks=Upcoming_Treks.objects.all()
            serializer=UpcomingTreksSerializer(upcoming_treks,many=True)
            return ResponseOk(
                {
                    "data": serializer.data,
                    "code": status.HTTP_200_OK,
                    "message": "Upcoming_Treks list",
                }
            )
        except:
            return ResponseBadRequest(
                {
                    "data": serializer.errors,
                    "code": status.HTTP_400_BAD_REQUEST,
                    "message": "Upcoming_Treks Does Not Exist",
                }
            )




class CreateUpcomingTreks(APIView):
    """
    Create Upcoming_Treks
    """

    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.JWTAuthentication]
    parser_classes = (FormParser, MultiPartParser)


    @swagger_auto_schema(
        operation_description="create Upcoming_Treks",
        request_body=UpcomingTreksSerializer,
    )
    @csrf_exempt
    def post(self, request):
        serializer = UpcomingTreksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return ResponseOk(
                {
                    "data": serializer.data,
                    "code": status.HTTP_200_OK,
                    "message": "Upcoming_Treks created succesfully",
                }
            )
            return ResponseBadRequest(
                {
                    "data": serializer.errors,
                    "code": status.HTTP_400_BAD_REQUEST,
                    "message": "Upcoming_Treks is not valid",
                }
            )



class GetUpcomingTreks(APIView):
    """
    Get Upcoming_Treks by pk
    """
    
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.JWTAuthentication]

    csrf_exempt
    def get_object(self, pk):
        try:
            return Upcoming_Treks.objects.get(pk=pk)
        except Upcoming_Treks.DoesNotExist:
            raise ResponseNotFound()

    def get(self, request, pk):
        try:
            upcoming_treks = self.get_object(pk)
            serializer = UpcomingTreksSerializer(upcoming_treks)
            return ResponseOk(
                {
                    "data": serializer.data,
                    "code": status.HTTP_200_OK,
                    "message": "get Upcoming_Treks successfully",
                }
            )
        except:
            return ResponseBadRequest(
                {
                    "data": None,
                    "code": status.HTTP_400_BAD_REQUEST,
                    "message": "Upcoming_Treks Does Not Exist",
                }
            )




class UpdateUpcomingTreks(APIView):
    """
    Update Upcoming_Treks
    """

    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.JWTAuthentication]
    parser_classes = (FormParser, MultiPartParser)


    def get_object(self, pk):
        try:
            return Upcoming_Treks.objects.get(pk=pk)
        except Upcoming_Treks.DoesNotExist:
            raise ResponseNotFound()

    @swagger_auto_schema(
        operation_description="update Upcoming_Treks",
        request_body=UpcomingTreksSerializer,
    )
    @csrf_exempt
    def put(self, request, pk):
        try:
            upcoming_treks = self.get_object(pk)
            serializer = UpcomingTreksSerializer(upcoming_treks, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return ResponseOk(
                    {
                        "data": serializer.data,
                        "code": status.HTTP_200_OK,
                        "message": "Upcoming_Treks updated successfully",
                    }
                )
            else:
                return ResponseBadRequest(
                    {
                        "data": serializer.errors,
                        "code": status.HTTP_400_BAD_REQUEST,
                        "message": "Upcoming_Treks Not valid",
                    }
                )
        except:
            return ResponseBadRequest(
                {
                    "data": None,
                    "code": status.HTTP_400_BAD_REQUEST,
                    "message": "Upcoming_Treks Does Not Exist",
                }
            )



class DeleteUpcomingTreks(APIView):
    """
    Delete Upcoming_Treks
    """

    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.JWTAuthentication]

    @csrf_exempt
    def get_object(self, pk):
        try:
            return Upcoming_Treks.objects.get(pk=pk)
        except Upcoming_Treks.DoesNotExist:
            raise ResponseNotFound()

    def delete(self, request, pk):
        try:
            upcoming_treks = self.get_object(pk)
            upcoming_treks.delete()
            return ResponseOk(
                {
                    "data": None,
                    "code": status.HTTP_200_OK,
                    "message": "Upcoming_Treks deleted Successfully",
                }
            )
        except:
            return ResponseBadRequest(
                {
                    "data": None,
                    "code": status.HTTP_400_BAD_REQUEST,
                    "message": "Upcoming_Treks Does Not Exist",
                }
            )


class GetAllUpcomingRoadTrips(APIView):
    """
    Get All Upcoming_Road_Trips
    """
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.JWTAuthentication]

    @csrf_exempt
    def get(self, request):
        try:
            upcoming_road_trips=Upcoming_Road_Trips.objects.all()
            serializer=UpcomingRoadTripsSerializer(upcoming_road_trips,many=True)
            return ResponseOk(
                {
                    "data": serializer.data,
                    "code": status.HTTP_200_OK,
                    "message": "Upcoming_Road_Trips list",
                }
            )
        except:
            return ResponseBadRequest(
                {
                    "data": serializer.errors,
                    "code": status.HTTP_400_BAD_REQUEST,
                    "message": "Upcoming_Road_Trips Does Not Exist",
                }
            )




class CreateUpcomingRoadTrips(APIView):
    """
    Create Upcoming_Road_Trips
    """

    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.JWTAuthentication]
    parser_classes = (FormParser, MultiPartParser)


    @swagger_auto_schema(
        operation_description="create Upcoming_Road_Trips",
        request_body=UpcomingRoadTripsSerializer,
    )
    @csrf_exempt
    def post(self, request):
        serializer = UpcomingRoadTripsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return ResponseOk(
                {
                    "data": serializer.data,
                    "code": status.HTTP_200_OK,
                    "message": "Upcoming_Road_Trips created succesfully",
                }
            )
            return ResponseBadRequest(
                {
                    "data": serializer.errors,
                    "code": status.HTTP_400_BAD_REQUEST,
                    "message": "Upcoming_Road_Trips is not valid",
                }
            )



class GetUpcomingRoadTrips(APIView):
    """
    Get Upcoming_Road_Trips by pk
    """
    
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.JWTAuthentication]

    csrf_exempt
    def get_object(self, pk):
        try:
            return Upcoming_Road_Trips.objects.get(pk=pk)
        except Upcoming_Road_Trips.DoesNotExist:
            raise ResponseNotFound()

    def get(self, request, pk):
        try:
            upcoming_road_trips = self.get_object(pk)
            serializer = UpcomingRoadTripsSerializer(upcoming_road_trips)
            return ResponseOk(
                {
                    "data": serializer.data,
                    "code": status.HTTP_200_OK,
                    "message": "get Upcoming_Road_Trips successfully",
                }
            )
        except:
            return ResponseBadRequest(
                {
                    "data": None,
                    "code": status.HTTP_400_BAD_REQUEST,
                    "message": "Upcoming_Road_Trips Does Not Exist",
                }
            )


class UpdateUpcomingRoadTrips(APIView):
    """
    Update Upcoming_Road_Trips
    """

    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.JWTAuthentication]
    parser_classes = (FormParser, MultiPartParser)


    def get_object(self, pk):
        try:
            return Upcoming_Road_Trips.objects.get(pk=pk)
        except Upcoming_Road_Trips.DoesNotExist:
            raise ResponseNotFound()

    @swagger_auto_schema(
        operation_description="update Upcoming_Road_Trips",
        request_body=UpcomingRoadTripsSerializer,
    )
    @csrf_exempt
    def put(self, request, pk):
        try:
            upcoming_road_trips = self.get_object(pk)
            serializer = UpcomingRoadTripsSerializer(upcoming_road_trips, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return ResponseOk(
                    {
                        "data": serializer.data,
                        "code": status.HTTP_200_OK,
                        "message": "Upcoming_Road_Trips updated successfully",
                    }
                )
            else:
                return ResponseBadRequest(
                    {
                        "data": serializer.errors,
                        "code": status.HTTP_400_BAD_REQUEST,
                        "message": "Upcoming_Road_Trips Not valid",
                    }
                )
        except:
            return ResponseBadRequest(
                {
                    "data": None,
                    "code": status.HTTP_400_BAD_REQUEST,
                    "message": "Upcoming_Road_Trips Does Not Exist",
                }
            )



class DeleteUpcomingRoadTrips(APIView):
    """
    Delete Upcoming_Road_Trips
    """

    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.JWTAuthentication]

    @csrf_exempt
    def get_object(self, pk):
        try:
            return Upcoming_Road_Trips.objects.get(pk=pk)
        except Upcoming_Road_Trips.DoesNotExist:
            raise ResponseNotFound()

    def delete(self, request, pk):
        try:
            upcoming_road_trips = self.get_object(pk)
            upcoming_road_trips.delete()
            return ResponseOk(
                {
                    "data": None,
                    "code": status.HTTP_200_OK,
                    "message": "Upcoming_Road_Trips deleted Successfully",
                }
            )
        except:
            return ResponseBadRequest(
                {
                    "data": None,
                    "code": status.HTTP_400_BAD_REQUEST,
                    "message": "Upcoming_Road_Trips Does Not Exist",
                }
            )