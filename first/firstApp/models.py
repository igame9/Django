from django.db import models


class Student(models.Model):
    nameStudent = models.CharField("Имя стдента", max_length=20) # max_length - максимальная длина текста
    familyStudent = models.CharField("Фамилия студента", max_length=20)
    averageScore = models.FloatField("Средний балл")

    class Meta: # для руссификации в админке
        verbose_name = "Студент"
        verbose_name_plural = "Студенты"
