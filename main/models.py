from cProfile import label
from codecs import charmap_build
from pickle import TRUE
from turtle import ondrag
from django.db import models
from django.contrib.auth.models import User


class Course(models.Model):
    name=models.CharField(max_length=200, null=True)
    short_description=models.CharField(max_length=200, null=True)
    long_description=models.CharField(max_length=1000, null=True)


    def __str__(self):
        return self.name

class Task(models.Model):
    TYPE = (
        ('Homework', 'Homework'),
        ('Group Project', 'Group Project')
    )
    course=models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True)
    type = models.CharField(max_length=200, null = True, choices = TYPE)
    name = models.CharField(max_length=200, null = True)
    deadline = models.DateTimeField(auto_now_add=False, null= True, editable=True)
    text = models.CharField(max_length=2000, null=True, blank=True)

    def __str__(self):
        return self.name

class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, db_column='course_lesson')
    name=models.CharField(max_length=200, null=True)
    short_description=models.CharField(max_length=200, null=True)
    long_description=models.CharField(max_length=1000, null=True)
    video = models.CharField(max_length=1000, null=True)
    video_description = models.CharField(max_length=2000, null=True)
    contents = models.CharField(max_length=2000, null=True)

    def __str__(self):
        return self.name

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class TaskStudent(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, null=True, blank=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True, blank=True)
    status = models.CharField(max_length=200, null=True, default='NEW')
    quickA = models.BooleanField(default=True)

class Solution(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, null=True, blank=True)
    solution = models.FileField(null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True, blank=True)