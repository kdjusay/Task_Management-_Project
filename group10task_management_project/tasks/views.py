from django.shortcuts import render

# Create your views here.

#Retrieve all users(GET)
from django.http import JsonResponse
from .models import User


def get_users(request):
    users = list(User.objects.values('id', 'username', 'email', 'created_at'))
    return JsonResponse(users, safe=False)

#Create a User(POST)
import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def create_user(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user = User.objects.create(username=data['username'], email=data['email'])
        return JsonResponse({'id': user.id, 'message': 'User created successfully'}, status=201)
    

#Retrieve all Tasks(GET)
from .models import Task


def get_tasks(request):
    tasks = list(Task.objects.values('id', 'title', 'description', 'is_completed', 'user', 'created_at'))
    return JsonResponse(tasks, safe=False)


#Create a Post(POST)
@csrf_exempt
def create_task(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user = User.objects.get(id=data['user'])
        task = Task.objects.create(title=data['title'], description=data.get('description', ''), user=user)
        return JsonResponse({'id': task.id, 'message': 'Task created successfully'}, status=201)


