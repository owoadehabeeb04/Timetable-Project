from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Level(models.Model):
    level = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.level

class Timetable(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    day = models.CharField(max_length=50)  # e.g., Monday, Tuesday
    time = models.TimeField()
    course = models.CharField(max_length=200)
    lecturer = models.CharField(max_length=200)
    venue = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.department.name} {self.level.level} {self.day} {self.time} - {self.course}"
