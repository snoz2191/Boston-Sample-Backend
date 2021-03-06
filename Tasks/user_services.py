from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Login, Status
from .serializers import LoginSerializer, UserSerializer, StatusSerializer
from .utils import STATUS_OK, STATUS_PARAMETERS_INVALID, STATUS_USER_INVALID, STATUS_USER_INACTIVE


class LoginService(APIView):

    def post(self,request):
    
      # Validate the Login be a proper request (Json Parseable)
      try:
        l = LoginSerializer(data=request.data)
      except:
        status = STATUS_PARAMETERS_INVALID
        return Response(StatusSerializer(status).data)

      # Validates format
      if l.is_valid():
        try:
          u = User.objects.get(username=l.validated_data["username"])
        except User.DoesNotExist:
          status = STATUS_USER_INVALID
          return Response(StatusSerializer(status).data)

      # If is invalid the response are the errors
      else: 
        return Response(l.errors)

      # Authenticates the user
      user = authenticate(username=u.username, password=l.validated_data["password"])

      # If user exists
      if user is not None:

        # If the user is active in the DB
        if user.is_active:
          login(request, user)
          status = STATUS_OK
          return Response(StatusSerializer(status).data)

        else: # User inactive
          status = STATUS_USER_INACTIVE
          return Response(StatusSerializer(status).data)
      
      else: # User doesnt exist
        status = STATUS_USER_INVALID
        return Response(StatusSerializer(status).data)

    def delete(self,request):
      logout(request)
      status = STATUS_OK
      return Response(StatusSerializer(status).data)

class SignUpService(APIView):
  def post(self,request):
    try:
      u = UserSerializer(data=request.data)
    except:
      status = STATUS_PARAMETERS_INVALID
      return Response(StatusSerializer(status).data)

    if u.is_valid():
      # Set hash password
      u.validated_data["password"] = make_password(password=u.validated_data["password"])
      u.save()
      status = STATUS_OK
      return Response(StatusSerializer(status).data)
    else:
      return Response(u.errors)
