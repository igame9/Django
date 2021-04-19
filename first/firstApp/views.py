from django.http import HttpResponseGone, HttpResponse
from django.shortcuts import render
from .models import Student
from django.contrib import messages


# from django.http import JsonResponse


def tableStudents(request):
    queryResult = Student.objects.all()
    return render(request, "templates/pageWithStudents.html", {"student": queryResult})


def get(request):
    responseData = {}
    for person in Student.objects.all():
        responseData.setdefault(str(person.averageScore), str(person.familyStudent) + " " + str(person.nameStudent))
    return HttpResponse(str(responseData).encode("utf-8"))


def viewPageWithAdd(request):
    return render(request, "templates/addStudent.html")


def addStudents(request):
    if request.method == 'POST':
        nameStudent = request.POST.get("inputName")
        familyStudent = request.POST.get("familyInput")
        averageMarkStudent = request.POST.get("averageMark")
        messages.success(request, 'Данные отправлены на сервер')
        print(nameStudent + familyStudent + averageMarkStudent)
        return render(request, "templates/addStudent.html")
    else:
        return HttpResponse(status=400)
