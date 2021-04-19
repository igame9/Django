from django.urls import path
from . import views  # view из корня

urlpatterns = [
    path("get/", views.get, name="_jsonData_"),
    path("", views.tableStudents, name="_tableStudents_"),
    path("new/", views.viewPageWithAdd, name="_addStudent_"),
    path("newStudent/", views.addStudents, name="_newStudent_"),
]
