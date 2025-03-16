from rest_framework import generics
from todolistapp.models import Task, Taskers
from .serializers import TaskersSerializer, TaskSerializer

# Create your views here.

# CRUD operations for the Tasker
class TaskersListCreate(generics.ListCreateAPIView):
    queryset = Taskers.objects.all()
    serializer_class = TaskersSerializer
class TaskerRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Taskers.objects.all()
    serializer_class = TaskersSerializer

    # CRUD OPERATIONS FOR TASKS
class TaskListCreate(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskRetrieveUpdateDelete(generics.RetrieveUpdateAPIView):
    queryset = Taskers.objects.all()
    serializer_class = TaskSerializer
