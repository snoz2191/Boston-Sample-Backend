from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from Tasks.utils import STATUS_PARAMETERS_INVALID, STATUS_OK, STATUS_TASK_CREATOR_REQUIRED

from .serializers import TaskSerializer, StatusSerializer
from .models import Task

# List Tasks
class TaskListService(APIView):
    def get(self, request):
        task_list = TaskSerializer(Task.objects.all(), many=True)
        return Response(task_list.data)

    def post(self, request):
        try:
            task = TaskSerializer(data=request.data)
        except:
            status = STATUS_PARAMETERS_INVALID
            return Response(StatusSerializer(status).data)

        try:
            task.initial_data["creator"] = User.objects.get(username=task.initial_data["creator"]).pk
        except User.DoesNotExist:
            status = STATUS_PARAMETERS_INVALID
            return Response(StatusSerializer(status).data)
        except KeyError:
            status = STATUS_TASK_CREATOR_REQUIRED
            return Response(StatusSerializer(status).data)

        if task.is_valid():
            task.save()
            status = STATUS_OK
            return Response(StatusSerializer(status).data)
        else:
            return Response(task.errors)