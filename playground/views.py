from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse, JsonResponse, FileResponse
from django.views.decorators.csrf import csrf_exempt
import os
import json

def getSmth(request):
    data = {'message': 'GET request received'}
    return JsonResponse(data)
def postSmth(request):
    try:
        data = json.loads(request.body)
        field_value = data.get('field_name', None)
        return JsonResponse(data)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON data received'}, status=400)
def putSmth(request):
    data = {'message': 'PUT request received'}
    return JsonResponse(data)
def deleteSmth(request, *args, **kwargs):
    data = {'message': 'DELETE request received'}
    return JsonResponse(data)



@csrf_exempt
def handleCrud(request):
    if request.method == 'GET':
        return getSmth(request)
    elif request.method == 'POST':
        return postSmth(request)
    elif request.method == 'PUT':
        return putSmth(request)
    elif request.method == 'DELETE':
        return deleteSmth(request)
    else:
        return JsonResponse({'message': 'Unsupported HTTP method'})


def sendHTML(request):
    return render(request, 'index.html', {'items': [{'name': 'Thomas'}, {'name': 'John'}]})


def sendIMG(request):
    return FileResponse(open('C:\\Users\\1levk\\PycharmProjects\\djangoPrj\\firstDjango\\static\\images\\img.png', 'rb'), content_type='image/png')


def sendJSON(request):
    return JsonResponse({'message': 'JSON received'})


def sayHello(request):
    return HttpResponse("Hello, Django!")


def set_cookie(request):
    response = HttpResponse("Cookie set!")
    response.set_cookie('my_cookie', 'Hello from server!', max_age=100000000, httponly=False)
    return response


def get_cookie(request):
    print(request.COOKIES)
    print(request.META)
    my_cookie_value = request.COOKIES.get('my_cookie', 'Cookie not set')
    return HttpResponse(f"Value of my_cookie: {my_cookie_value}")
