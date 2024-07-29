from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .serializers import carSerializer

from .models import Car

# Create your views here.


@api_view(["POST"])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def addCar(request):
    if request.method == "POST":
        serializer = carSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response({
                "responseCode": "000",
                "responseMessage": "Car added successfully",
                "data": serializer.data
            })
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def getCar(request):
    if request.method == "GET":
        allcars = Car.objects.all()
        serializer = carSerializer(instance=allcars, many=True)
        return Response({
            "responseCode": "000",
            "responseMessage": "List of cars",
            "data": serializer.data})
