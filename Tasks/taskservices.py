
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import TaskSerializer
from .models import Task

# List Tasks
class TaskListService(APIView):
  def get(self, request):
    task_list = TaskSerializer(Task.objects.all(), many=True)
    return Response(task_list.data)