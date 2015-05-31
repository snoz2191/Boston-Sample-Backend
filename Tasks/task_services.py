from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from Tasks.utils import *

from .serializers import TaskSerializer, StatusSerializer
from .models import Task

# List Tasks
class TaskListService(APIView):
    # GET method
    def get(self, request):
        task_list = TaskSerializer(Task.objects.all(), many=True)
        return Response(task_list.data)
        
    def post(self,request):
        try:
            task = TaskSerializer(data=request.data)
            if task.is_valid():
                task.save()
                status = STATUS_OK
                return Response(StatusSerializer(status).data)
            else:
                return Response(task.errors)

        except:
            status = STATUS_PARAMETERS_INVALID
            return Response(StatusSerializer(status).data)


