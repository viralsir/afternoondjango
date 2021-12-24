from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
def greetings(request,username):
    return HttpResponse(f"<h1>Hello {username}</h1>");