from django.urls import path
from .views import viewtask
urlpatterns=[
        path("view/",viewtask,name="task-view")
]