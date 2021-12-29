from django.urls import path
from .views import *
urlpatterns=[
    path("add/",newstudent,name="new-student"),
    path("view/",viewstudent,name="view-student")
]