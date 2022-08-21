from django.contrib import admin
from .models import Course,Lesson,Task,Student
# Register your models here.

admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(Task)