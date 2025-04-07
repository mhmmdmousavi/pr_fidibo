from django.shortcuts import render
from django.http.response import HttpResponse

def hello_response(request):
    return HttpResponse("hello, this is home page!")

