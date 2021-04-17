from django.contrib import admin
from .models import Student

# регистрируем приложения в админке
admin.site.register(Student)
