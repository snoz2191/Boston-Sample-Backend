from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from Tasks.models import Login, Status
from Tasks.serializers import LoginSerializer, UserSerializer, StatusSerializer
from django.views.decorators.csrf import csrf_exempt


class LoginService(APIView):

    def post(self,request):
      l = LoginSerializer(data=request.data)

      # Validates format
      if l.is_valid():
        u = User.objects.get(username=l.validated_data["username"])
      else:
        status = Status(code="INVALID",msg="The format in the request is invalid")
        return Response(StatusSerializer(status).data)

      # Authenticates the user
      user = authenticate(username=u.username, password=l.validated_data["password"])

      # If user exists
      if user is not None:

        # If the user is active in the DB
        if user.is_active:
          login(request, user)
          status = Status(code="OK",msg="OK")
          return Response(StatusSerializer(status).data)

        else:
          return Response("Error! User is inactive in DB")
      
      else:
        return Response("User is none, he doesn't exist")

    def delete(self,request):
      logout(request)
      status = Status(code="OK",msg="OK")
      return Response(StatusSerializer(status).data)
