from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from Tasks.utils import STATUS_PARAMETERS_INVALID, STATUS_OK, STATUS_EXECUTION_NOT_EXISTS

from .serializers import TaskSerializer, StatusSerializer, ExecutionSerializer
from .models import Execution

# List Tasks
class ExecutionListService(APIView):
  #GET method
  def get(self, request):
    execution_list = ExecutionSerializer(Execution.objects.all(), many=True)
    return Response(execution_list.data)

  #POST method
  def post(self,request):
    try:
      #request.data["creator"] = User.objects.get(username=request.data["creator"]).username
      execution = ExecutionSerializer(data=request.data)
      
    except:
      return Response(StatusSerializer(STATUS_PARAMETERS_INVALID).data)

    if execution.is_valid():
      execution.save()
      return Response(StatusSerializer(STATUS_OK).data)
    else:
      return Response(execution.errors)

class ExecutionItemService(APIView):
  
  #GET Method
  def get(self, request, execution_id):
    try:
      execution = Execution.objects.get(pk=execution_id)
    except ObjectDoesNotExist:
      status = STATUS_EXECUTION_NOT_EXISTS
      return Response(StatusSerializer(status).data)

    execution_s = ExecutionSerializer(execution)  
    return Response(execution_s.data)
  #DELETE Method
  def delete(self, request, execution_id):
    try:
      execution = Execution.objects.get(pk=execution_id)
    except ObjectDoesNotExist:
      status = STATUS_EXECUTION_NOT_EXISTS
      return Response(StatusSerializer(status).data)

    execution.delete()
    return Response(StatusSerializer(STATUS_OK).data)

  # Edit an Execution
  def put(self, request, execution_id):
    try:
      execution = Execution.objects.get(pk=execution_id)
    except ObjectDoesNotExist:
      status = STATUS_EXECUTION_NOT_EXISTS
      return Response(StatusSerializer(status).data)
    new_execution = ExecutionSerializer(execution,data=request.data, partial=True)
    if new_execution.is_valid():
      new_execution.save()
      return Response(StatusSerializer(STATUS_OK).data)
    else:
      return Response(new_execution.errors)

