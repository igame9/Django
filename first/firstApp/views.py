from django.http import HttpResponseGone, HttpResponse
from django.shortcuts import render
from .models import Student
# from django.http import JsonResponse


def tableStudents(request):
    queryResult = Student.objects.all()

    return render(request, "templates/pageWithStudents.html", {"student":queryResult})


def get(request):
    responseData = {}
    for person in Student.objects.all():
        responseData.setdefault(str(person.averageScore),  str(person.familyStudent) + " " + str(person.nameStudent))
    return HttpResponse(str(responseData).encode("utf-8"))
