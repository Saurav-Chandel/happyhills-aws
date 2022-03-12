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


class GetAllReview(APIView):
    """
    Get All Review
    """
    # permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.JWTAuthentication]

    @csrf_exempt
    def get(self, request):
        try:
            review=Review.objects.all()
            serializer=ReviewSerializer(review,many=True)
            return ResponseOk(
                {
                    "data": serializer.data,
                    "code": status.HTTP_200_OK,
                    "message": "Review list",
                }
            )
        except:
            return ResponseBadRequest(
                {
                    "data": serializer.errors,
                    "code": status.HTTP_400_BAD_REQUEST,
                    "message": "Review Does Not Exist",
                }
            )




class CreateReview(APIView):
    """
    Create Review
    """

    # permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.JWTAuthentication]
    parser_classes = (FormParser, MultiPartParser)


    @swagger_auto_schema(
        operation_description="create Review",
        request_body=ReviewSerializer,
    )
    @csrf_exempt
    def post(self, request):
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return ResponseOk(
                {
                    "data": serializer.data,
                    "code": status.HTTP_200_OK,
                    "message": "Review created succesfully",
                }
            )
            return ResponseBadRequest(
                {
                    "data": serializer.errors,
                    "code": status.HTTP_400_BAD_REQUEST,
                    "message": "Review is not valid",
                }
            )



class GetReview(APIView):
    """
    Get Review by pk
    """
    
    # permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.JWTAuthentication]

    csrf_exempt

    def get_object(self, pk):
        try:
            return Review.objects.get(pk=pk)
        except Review.DoesNotExist:
            raise ResponseNotFound()

    def get(self, request, pk):
        try:
            review = self.get_object(pk)
            serializer = ReviewSerializer(review)
            return ResponseOk(
                {
                    "data": serializer.data,
                    "code": status.HTTP_200_OK,
                    "message": "get Review successfully",
                }
            )
        except:
            return ResponseBadRequest(
                {
                    "data": None,
                    "code": status.HTTP_400_BAD_REQUEST,
                    "message": "Review Does Not Exist",
                }
            )




class UpdateReview(APIView):
    """
    Update Review
    """

    # permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.JWTAuthentication]
    parser_classes = (FormParser, MultiPartParser)


    def get_object(self, pk):
        try:
            return Review.objects.get(pk=pk)
        except Review.DoesNotExist:
            raise ResponseNotFound()

    @swagger_auto_schema(
        operation_description="create Review",
        request_body=ReviewSerializer,
    )
    @csrf_exempt
    def put(self, request, pk):
        try:
            review = self.get_object(pk)
            serializer = ReviewSerializer(review, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return ResponseOk(
                    {
                        "data": serializer.data,
                        "code": status.HTTP_200_OK,
                        "message": "Review updated successfully",
                    }
                )
            else:
                return ResponseBadRequest(
                    {
                        "data": serializer.errors,
                        "code": status.HTTP_400_BAD_REQUEST,
                        "message": "Review Not valid",
                    }
                )
        except:
            return ResponseBadRequest(
                {
                    "data": None,
                    "code": status.HTTP_400_BAD_REQUEST,
                    "message": "Review Does Not Exist",
                }
            )



class DeleteReview(APIView):
    """
    Delete Review
    """

    # permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.JWTAuthentication]

    @csrf_exempt
    def get_object(self, pk):
        try:
            return Review.objects.get(pk=pk)
        except Review.DoesNotExist:
            raise ResponseNotFound()

    def delete(self, request, pk):
        try:
            review = self.get_object(pk)
            review.delete()
            return ResponseOk(
                {
                    "data": None,
                    "code": status.HTTP_200_OK,
                    "message": "Review deleted Successfully",
                }
            )
        except:
            return ResponseBadRequest(
                {
                    "data": None,
                    "code": status.HTTP_400_BAD_REQUEST,
                    "message": "Review Does Not Exist",
                }
            )


