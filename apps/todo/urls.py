from django.urls import path
from apps.todo import views

urlpatterns = [
    path('', views.todolist, name='todolist'),
    path('delete', views.delete_tasks, name='delete_tasks'),
    path('delete/<task_id>', views.delete_task, name='delete_task'),
    path('edit/<task_id>', views.edit_task, name='edit_task'),
    path('complete', views.complete_tasks, name='complete_tasks'),
    path('complete/<task_id>', views.complete_task, name='complete_task'),
    path('pending/<task_id>', views.pending_task, name='pending_task'),
]