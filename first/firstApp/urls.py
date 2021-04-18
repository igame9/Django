from django.urls import path
from . import views  # view из корня

urlpatterns = [
    path("get/", views.get, name="_jsonData_"),
    path("", views.tableStudents, name="_tableStudents_"),
]
