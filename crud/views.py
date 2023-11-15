# Python imports 
import io

# Django Imports
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Local Imports
from .models import User
from .serializers import UserSerializer

# Rest FrameWork Imports
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

# Views
@csrf_exempt
def index(request):
  if request.method == 'POST':
    stream = io.BytesIO(request.body)
    python_data = JSONParser().parse(stream)
    serializer = UserSerializer(data=python_data)

    if serializer.is_valid():
      serializer.save()
      response = {'msg': 'Data Create Successfully'}
    else:
      response = {'errors': serializer.errors}
    json_data = JSONRenderer().render(response)
    return HttpResponse(json_data, content_type='application/json')

  else:
    query_set = User.objects.all()
    serializer = UserSerializer(query_set, many=True)
    return JsonResponse(serializer.data, safe=False)

def show(request, pk):
  user = User.objects.get(pk=pk)
  serializer = UserSerializer(user)
  return JsonResponse(serializer.data)

@csrf_exempt
def update(request, pk):
  if request.method == 'PATCH':
    stream = io.BytesIO(request.body)
    python_data = JSONParser().parse(stream)
    user = User.objects.get(pk=pk)
    serializer = UserSerializer(user, data=python_data, partial=True)
    
    if serializer.is_valid():
      serializer.save()
      response = {'msg': 'Data Updated Successfully'}
    else:
      response = {'errors': serializer.errors}
    json_data = JSONRenderer().render(response)
    return HttpResponse(json_data, content_type='application/json')

@csrf_exempt
def delete(request, pk):
  if request.method == 'DELETE':
    user = User.objects.get(pk=pk)
    user.delete()
    response = {'msg': 'Data deleted successfully'}
    json_response = JSONRenderer().render(response)
    return HttpResponse(json_response, content_type='application/json')

