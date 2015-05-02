from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from Tasks.models import Login, LoginSerializer, UserSerializer, Status, StatusSerializer
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

      if user is not None:
        if user.is_active:
          login(request, user)
          status = Status(code="OK",msg="OK")
          return Response(StatusSerializer(status).data)

        else:
          return Response("Error!")
      else:
        return Response("User is none")
    def delete(self,request):
      logout(request)
      status = Status(code="OK",msg="OK")
      return Response(StatusSerializer(status).data)
