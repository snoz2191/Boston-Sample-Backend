from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from Tasks.utils import STATUS_PARAMETERS_INVALID, STATUS_OK, STATUS_TASK_CREATOR_REQUIRED, STATUS_TASK_NOT_FOUND

from .serializers import TaskSerializer, StatusSerializer
from .models import Task

# List Tasks
class TaskListService(APIView):
    #GET method
    def get(self, request):
        id = self.request.query_params.get('id',None)

        if id is not None:
            try:
                task = Task.objects.get(id=id)
            except Task.DoesNotExist:
                status = STATUS_TASK_NOT_FOUND
                return Response(StatusSerializer(status).data)

            response = TaskSerializer(task).data
            response['status'] = StatusSerializer(STATUS_OK).data
            return Response(response)

        else:
            task_list = TaskSerializer(Task.objects.all(), many=True)
            return Response(task_list.data)

    #POST method
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
        else:
            status = STATUS_PARAMETERS_INVALID

        return Response(StatusSerializer(status).data)

    #DELETE Method
    def delete(self, request):
        id = self.request.query_params.get('id',None)

        if id is not None:
            Task.objects.filter(id=id).delete()
            status = STATUS_OK
        else:
            status = STATUS_PARAMETERS_INVALID

        return Response(StatusSerializer(status).data)

    #PUT Method
    def put(self, request):
        id = self.request.query_params.get('id',None)

        if id is not None:

            try:
                task = TaskSerializer(data=request.data)
            except:
                status = STATUS_PARAMETERS_INVALID
                return Response(StatusSerializer(status).data)

            try:
                t = Task.objects.get(id=id)
            except Task.DoesNotExist:
                status = STATUS_TASK_NOT_FOUND
                return Response(StatusSerializer(status).data)

            task.initial_data['creator'] = t.creator.pk

            if task.is_valid():
                t.name = task.validated_data['name']
                t.category = task.validated_data['category']
                t.description = task.validated_data['description']
                t.save()
                status = STATUS_OK
            else:
                status = STATUS_PARAMETERS_INVALID

        else:
            status = STATUS_PARAMETERS_INVALID

        return Response(StatusSerializer(status).data)
