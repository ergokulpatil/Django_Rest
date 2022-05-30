from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.


def index(request):
    return HttpResponse("Welcome to home page")


def learn_django(request):
    course_name={'cname':"Welcome to GGSF"}
    return render(request,'course/course1.html',course_name)
    #return HttpResponse("Hello Django")


def print_string(request):
    a="Gokul Patil"
    return HttpResponse(f'My name is {a}')