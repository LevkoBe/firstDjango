from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse, JsonResponse, FileResponse
from django.views.decorators.csrf import csrf_exempt
import os
import json

def sendHTML(request):
    return render(request, 'index.html', {'items': [{'name': 'Thomas'}, {'name': 'John'}]})