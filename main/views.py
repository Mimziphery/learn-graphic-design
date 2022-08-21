import imp
from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponse
from .models import Course, Lesson, Task, Student
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    courses = Course.objects.all()
    if request.user.is_authenticated:
        tasks = Task.objects.all().filter(quickA=True)
        user = request.user;
        student = Student.objects.get(user=user)
        return render(request, "home.html", {"tasks": tasks, "courses": courses, "student": student})
    else:
        return render(request, "home.html", {"courses": courses})

@login_required(login_url='/login')
def remove_task_from_quickAccsses(request,id):
    user = request.user;
    student = Student.objects.get(user=user)
    task = Task.objects.get(id=id)
    task.quickA = False
    task.save()
    tasks = Task.objects.all().filter(quickA=True)
    courses = Course.objects.all()
    return render(request, "home.html", {"tasks": tasks, "courses": courses, "student": student})

@login_required(login_url='/login')
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

@login_required(login_url='/login')
def illustration_lesson(response, lessonName):
    courses = Course.objects.all()
    course = Course.objects.get(name='Illustration')
    lesson = Lesson.objects.get(course=course.id, name=lessonName)
    contents = str(lesson.contents).split(",");
    return render(response, "lesson.html", {"courses": courses, "course": course, "contents": contents, "lesson": lesson})

@login_required(login_url='/login')
def photography_lesson(response, lessonName):
    courses = Course.objects.all()
    course = Course.objects.get(name='Photography')
    lesson = Lesson.objects.get(course=course.id, name=lessonName)
    contents = str(lesson.contents).split(",");
    return render(response, "lesson.html", {"courses": courses, "course": course, "contents": contents, "lesson": lesson})

@login_required(login_url='/login')
def typography_lesson(response, lessonName):
    courses = Course.objects.all()
    course = Course.objects.get(name='Typography')
    lesson = Lesson.objects.get(course=course.id, name=lessonName)
    contents = str(lesson.contents).split(",");
    return render(response, "lesson.html", {"courses": courses, "course": course, "contents": contents, "lesson": lesson})

@login_required(login_url='/login')
def task(response, taskid):
    courses = Course.objects.all()
    task = Task.objects.get(id=taskid)
    task.status = "Opened today"
    task.save()
    return render(response, "task.html", {"courses": courses, "task": task})

@login_required(login_url='/login')
def taskTrue(request, taskid):
    #task = Task.objects.get(id=taskid)
    user = request.user;
    student = Student.objects.get(user=user)
    task = student.tasks.all().get(id=taskid)
    task.quickA = True
    task.save()
    return HttpResponse('')

@login_required(login_url='/login')
def taskFalse(request, taskid):
    #task = Task.objects.get(id=taskid)
    user = request.user;
    student = Student.objects.get(user=user)
    task = student.tasks.all().get(id=taskid)
    task.quickA = False
    task.save()
    return HttpResponse('')
    
@login_required(login_url='/login')
def taskFinished(response, taskid):
    task = Task.objects.get(id=taskid)
    task.status = "Submited today"
    task.save()
    return HttpResponse('')
