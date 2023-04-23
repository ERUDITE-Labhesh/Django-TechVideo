from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def Homepage(request):
    return HttpResponse("Hello Welcome to Homepage!")

def Indexpage(request, data = None):
    return HttpResponse(f"This is the Endpoint {data}")
