from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view, authentication_classes,permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from .models import User
from rest_framework.response import Response
from .serializers import UserSerializer

# Create your views here.


@api_view(["POST"])
def register(request):
    if request.method == "POST":
        firstName = request.data["firstName"]
        lastName = request.data["lastName"]
        email = request.data["email"]
        gender = request.data["gender"]
        phoneNumber = request.data["phoneNumber"]
        password = request.data["password"]

        user = User()

        user.first_name = firstName
        user.last_name = lastName
        user.username = email
        user.email = email
        user.gender = gender
        user.phoneNumber = phoneNumber
        user.set_password(password)

        user.save()

        token, created = Token.objects.get_or_create(user=user)

        theUser = User.objects.get(username=email)
        serilizer = UserSerializer(instance=theUser)

        return Response({
            "responsecode": "000",
            "responseMessage": "User created successfuly",
            "data": serilizer.data,
            "token": token.key
        })


@api_view(["POST"])
def login(request):
    if request.method == "POST":
        email = request.data["email"]
        password = request.data["password"]

        user = get_object_or_404(User, email=email)

        if not user.check_password(password):
            return Response({
                "responsecode": "111",
                "responseMessage": "Invalid email or password",
                "data": ""
            })
        token, created = Token.objects.get_or_create(user=user)
        serializer = UserSerializer(instance=user)

        return Response({
            "responsecode": "000",
            "responseMessage": "User logged in successsfully",
            "data": serializer.data,
            "token": token.key
        })






@api_view(["POST"])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def logout(request):
    if request.method=="POST":
        request.user.auth_token.delete()
        return Response({
            "responseCode":"000",
            "responseMessage":"User logged out successfully"
		})