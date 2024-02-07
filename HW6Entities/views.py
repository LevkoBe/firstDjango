# views.py
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse, HttpResponseServerError
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json

from .models import Task


def main_page(request):
    return render(request, 'home.html')  # question: why?


def render_tasks(request):
    if request.method == 'GET':
        tasks = Task.objects.all()
        return render(request, 'entities.html', {'entities': tasks})

    elif request.method == 'POST':
        new_task = Task.objects.create(
            title=request.POST.get('title', ''),
            description=request.POST.get('description', ''),
            completed=request.POST.get('completed', False) == 'on',
            reminder=request.POST.get('reminder', None)
        )
        return JsonResponse({"message": "Task created successfully.", "id": new_task.id})


@csrf_exempt
@require_http_methods(["GET", "POST"])
def task_list(request):
    if request.method == 'GET':
        tasks = Task.objects.all()
        task_data = [{'id': task.id, 'title': task.title} for task in tasks]
        return JsonResponse({"tasks": task_data})

    elif request.method == 'POST':
        try:
            new_task = Task.objects.create(
                title=request.POST.get('title', ''),
                description=request.POST.get('description', ''),
                completed=request.POST.get('completed', False) == 'on',
                reminder=request.POST.get('reminder', None)
            )
            return JsonResponse({"message": "Task created successfully.", "id": new_task.id})
        except Exception as e:
            return HttpResponseServerError(content=f"Error creating task: {str(e)}")


@csrf_exempt
@require_http_methods(["GET", "DELETE"])
def specific_task(request, id):
    task = get_object_or_404(Task, id=id)

    if request.method == 'GET':
        task_data = {
            'id': task.id,
            'title': task.title,
            'description': task.description,
            'completed': task.completed,
            'reminder': task.reminder,
        }
        return JsonResponse(task_data)

    elif request.method == 'DELETE':
        try:
            task.delete()
            return JsonResponse({"message": "Task deleted successfully."})
        except Exception as e:
            return HttpResponseServerError(content=f"Error deleting task: {str(e)}")
