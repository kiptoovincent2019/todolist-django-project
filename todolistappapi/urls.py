from django.urls import path
from .views import (TaskersListCreate, TaskerRetrieveUpdateDelete, TaskListCreate, TaskRetrieveUpdateDelete)
urlpatterns = [
    # taskers CRUD
    path('taskers/', TaskersListCreate.as_view(), name='tasker-list-create'),
    path('taskers/<int:pk>', TaskRetrieveUpdateDelete.as_view(),name='tasker-retrieve-update-delete'),
    #tasks crud
    path('tasks/', TaskListCreate.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskRetrieveUpdateDelete.as_view(),name='task-retrieve-update-delete'),
]