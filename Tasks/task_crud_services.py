__author__ = 'domingo'
from rest_framework.views import APIView
from rest_framework.response import Response
from Tasks.utils import *

from .serializers import TaskSerializer, StatusSerializer
from .models import Task


class TaskCrudService(APIView):
    # GET method
    def get(self, request, id):
        try:
            task = Task.objects.get(id=id)
            response = TaskSerializer(task).data
            response['status'] = StatusSerializer(STATUS_OK).data
            return Response(response)
        except Task.DoesNotExist:
            status = STATUS_TASK_NOT_FOUND
            return Response(StatusSerializer(status).data)

    #DELETE Method
    def delete(self, request, id):
        try:
            task = Task.objects.get(id=id)
            task.delete()
            status = STATUS_OK
            return Response(StatusSerializer(status).data)
        except Task.DoesNotExist:
            status = STATUS_TASK_NOT_FOUND
            return Response(StatusSerializer(status).data)


    #PUT Method
    def put(self, request, id):
        try:
            t = Task.objects.get(id=id)

            new_task = TaskSerializer(t, data=request.data, partial=True)
            if new_task.is_valid():
                new_task.save()
                status = STATUS_OK
            else:
                status = STATUS_PARAMETERS_INVALID

            return Response(StatusSerializer(status).data)

        except Task.DoesNotExist:
            status = STATUS_TASK_NOT_FOUND
            return Response(StatusSerializer(status).data)