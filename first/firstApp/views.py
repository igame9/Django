from django.http import HttpResponseGone


def index(request):
    return HttpResponseGone("Привет")


def next(request):
    return HttpResponseGone("Некст")
