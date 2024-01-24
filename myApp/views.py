from django.shortcuts import render
from .models import MyModel

def index(request):
    instances = MyModel.objects.all()
    return render(request, 'index.html', {'instances': instances})
