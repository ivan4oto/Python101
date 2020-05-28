from django.db import models
from django.utils import timezone


class Course(models.Model):
    name = models.CharField(max_length=250, unique=True)
    description = models.TextField()
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(null=True)

    def __str__(self):
        return f'Course "{self.name}"'

    @property
    def duration(self):
        if self.end_date:
            return self.end_date - self.start_date


class Lecture(models.Model):
    name = models.CharField(max_length=250, unique=True)
    week = models.IntegerField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    url = models.URLField()

    def __str__(self):
        return f'Lecture "{self.name}"'


class Task(models.Model):
    name = models.CharField(max_length=250, unique=True)
    description = models.TextField()
    due_date = models.DateTimeField(null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    lecture = models.ForeignKey(Lecture, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'Task "{self.name}"'


class Solution(models.Model):
    date = models.DateTimeField(null=False, default=timezone.now)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    url = models.URLField()

    def __str__(self):
        return f'Solution "{self.url}"'