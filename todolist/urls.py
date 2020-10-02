from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create', views.create_task, name='tasks.create'),
    path('tasks/<int:task_id>', views.edit_task, name='tasks.edit'),
    path('delete/<int:task_id>', views.delete, name="delete"), 
]