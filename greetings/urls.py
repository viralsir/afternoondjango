from django.urls import path
from .views import greetings
urlpatterns=[
    path("home/<str:username>",greetings,name="greetings-home")
]