from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request,'EventManage/index.html')


def eventRegistration(request):
    return render(request,'EventManage/EventRegistration.html')