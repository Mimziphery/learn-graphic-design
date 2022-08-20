import imp
from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponse
from .models import Course, Lesson, Task
# Create your views here.

def index(response):
    tasks = Task.objects.all().filter(quickA=True)
    courses = Course.objects.all()
    return render(response, "home.html", {"tasks": tasks, "courses": courses})

def remove_task_from_quickAccsses(response,id):
    task = Task.objects.get(id=id)
    task.quickA = False
    task.save()
    tasks = Task.objects.all().filter(quickA=True)
    courses = Course.objects.all()
    return render(response, "home.html", {"tasks": tasks, "courses": courses})

def tasks(response):
    tasks = Task.objects.all()
    courses = Course.objects.all()
    return render(response, "tasks.html", {"tasks": tasks, "courses": courses})

def illustrationCourse(response):
    courses = Course.objects.all()
    course = Course.objects.get(name='Illustration')
    lessons = Lesson.objects.all().filter(course=course.id)
    return render(response, "course.html", {"courses": courses, "course": course, "lessons":lessons})

def typographyCourse(response):
    courses = Course.objects.all()
    course = courses.get(name='Typography')
    lessons = Lesson.objects.all().filter(course=course.id)
    return render(response, "course.html", {"courses": courses, "course":course, "lessons":lessons})

def photographyCourse(response):
    courses = Course.objects.all()
    course = courses.get(name='Photography')
    lessons = Lesson.objects.all().filter(course=course.id)
    
    return render(response, "course.html",{"courses": courses, "course": course, "lessons": lessons} )

def illustration_lesson(response, lessonName):
    courses = Course.objects.all()
    course = Course.objects.get(name='Illustration')
    lesson = Lesson.objects.get(course=course.id, name=lessonName)
    contents = str(lesson.contents).split(",");
    return render(response, "lesson.html", {"courses": courses, "course": course, "contents": contents, "lesson": lesson})

def photography_lesson(response, lessonName):
    courses = Course.objects.all()
    course = Course.objects.get(name='Photography')
    lesson = Lesson.objects.get(course=course.id, name=lessonName)
    contents = str(lesson.contents).split(",");
    return render(response, "lesson.html", {"courses": courses, "course": course, "contents": contents, "lesson": lesson})

def typography_lesson(response, lessonName):
    courses = Course.objects.all()
    course = Course.objects.get(name='Typography')
    lesson = Lesson.objects.get(course=course.id, name=lessonName)
    contents = str(lesson.contents).split(",");
    return render(response, "lesson.html", {"courses": courses, "course": course, "contents": contents, "lesson": lesson})

def task(response, taskid):
    courses = Course.objects.all()
    task = Task.objects.get(id=taskid)
    task.status = "Opened today"
    task.save()
    return render(response, "task.html", {"courses": courses, "task": task})

def taskTrue(response, taskid):
    task = Task.objects.get(id=taskid)
    task.quickA = True
    task.save()
    return HttpResponse('')

def taskFalse(response, taskid):
    task = Task.objects.get(id=taskid)
    task.quickA = False
    task.save()
    return HttpResponse('')

def taskFinished(response, taskid):
    task = Task.objects.get(id=taskid)
    task.status = "Submited today"
    task.save()
    return HttpResponse('')
