from django.http import HttpResponseGone, HttpResponse
from django.shortcuts import render
from .models import Student
from django.contrib import messages


# from django.http import JsonResponse

def isFloatOrInt(string):
    if string.isdigit():
        return True
    else:
        try:
            float(string)
            return True
        except ValueError:
            return False


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
        if nameStudent == '' or familyStudent == '' or averageMarkStudent == '' or not isFloatOrInt(averageMarkStudent):
            messages.warning(request, 'Данные некорректны')
            print(type(averageMarkStudent))
            return render(request, "templates/addStudent.html")
        else:
            messages.success(request, 'Данные отправлены на сервер')
            print(nameStudent + familyStudent + averageMarkStudent)
            student = Student(nameStudent=nameStudent, familyStudent=familyStudent, averageScore=averageMarkStudent)
            student.save()
            return render(request, "templates/addStudent.html")
    else:
        return HttpResponse(status=500)
