from django.urls import path
from HW6Entities.views import main_page, render_tasks, specific_task


urlpatterns = [
    path("", main_page, name='main_page'),
    path('tasks/', render_tasks, name='task_list'),
    path('tasks/<int:id>/', specific_task, name='specific_task'),
]

