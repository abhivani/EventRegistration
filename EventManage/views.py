from django.shortcuts import redirect, render



def index(request):
    return render(request,'EventManage/index.html')


def eventRegistration(request):
    return render(request,'EventManage/EventRegistration.html')

def login(request):
    return  render(request,'EventManage/login.html')
