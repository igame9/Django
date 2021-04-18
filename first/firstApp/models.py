from django.db import models


class Student(models.Model):
    nameStudent = models.CharField("Имя стдента", max_length=20)  # max_length - максимальная длина текста
    familyStudent = models.CharField("Фамилия студента", max_length=20)
    averageScore = models.FloatField("Средний балл")

    def __str__(self):
        return str(self.nameStudent) + str(self.familyStudent) + str(self.averageScore)

    class Meta:  # для руссификации в админке
        verbose_name = "Студент"
        verbose_name_plural = "Студенты"
