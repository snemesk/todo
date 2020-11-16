from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create', views.create_task, name='tasks.create'),
    path('delete/<int:task_id>', views.delete, name="delete"), 
        path('tasks2/<int:task_id>', views.edit_task2, name='tasks.edit2'),
]