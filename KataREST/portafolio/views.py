from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from .models import Image, Portafolio, CustomUser
import json

# Create your views here.

@csrf_exempt
def index(request):
    username = request.GET.get('username')
    private = request.GET.get('private')
    if(username == ""):
        portafolio_list = Portafolio.objects.all()
    else:
        portafolio_list = Portafolio.objects.filter(user__username=username).filter(private=private)

    return HttpResponse(serializers.serialize("json", portafolio_list))


@csrf_exempt
def addUser(request):
    if request.method == 'POST':
        json_user = json.loads(request.body)
        username = json_user['username']
        first_name = json_user['first_name']
        last_name = json_user['last_name']
        password = json_user['password']
        email = json_user['email']
        professional_profile = json_user['professional_profile']
        user_model = CustomUser.objects.create_user(username=username, password=password)
        user_model.first_name = first_name
        user_model.last_name = last_name
        user_model.email = email
        user_model.professional_profile = professional_profile
        user_model.save()
    return HttpResponse(serializers.serialize("json", [user_model]))
