from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login
from .forms import registerUser
import time
from rest_framework import viewsets
from .serializers import DataSerializer
from .models import Data
from rest_framework.response import Response
from rest_framework.decorators import api_view



#----------------------------Log In Page----------------------------#
def getLogin(request):
    if request.method == "POST":
        user = request.POST.get('user')
        password = request.POST.get('pass')
        auth = authenticate(request, username=user, password=password)
        if auth is not None:
            login(request, auth)
            return redirect('index')
        else:
            return HttpResponse("Login failed")
    return render(request, "login.html")

#----------------------------Sign In Page----------------------------#
def getRegister(request):
    form = registerUser(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return redirect('login')
    return render(request, 'registration.html', {"form": form})

#----------------------------Index Page----------------------------#
@login_required
def index(request):
    #gobal variable
    inputValues = '1'
    searchValues = '2'


    if request.method == "POST":
        inputValues = request.POST.get('inputValues')
        searchValues = request.POST.get('searchValues')

    if searchValues in inputValues:
        data = "True"

        #Current user id
        current_user = request.user
        current_user = current_user.id

        # current time
        c_time = time.time()

        #desending order
        li = list(inputValues.split(","))
        li.sort(reverse=True)

        # Store data in database
        data_instance_user = Data.objects.create(user_id=current_user, timestamp=c_time, input_values=li)
        data_instance_user.save()

        return render(request, "index.html",{"data":data})

    else:
        data = "false"
        return render(request, "index.html",{"data":data})
    #return render(request, "index.html")


#----------------------------REST API----------------------------#
@api_view(['GET'])
def dataViewSet(request):
    if request.method == 'GET':
        posts = Data.objects.all()
        serializer = DataSerializer(posts, many=True)
        return Response(serializer.data)
