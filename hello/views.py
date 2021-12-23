#http : hypertext transfer protocall
from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.

def sayhello(request):
    return HttpResponse("<h1 style='color:red;text-align:center'>wel come to the world of django</h1>");

def home(request):
    return HttpResponse("<a href='/aboutus'>About us </a> | <a href='/contact'>Contact us </a>");

def aboutus(request):
    return HttpResponse("<h1>About us Page </h1>");

def contactus(request):
    return HttpResponse("<h1>Contact us Page</h1>");