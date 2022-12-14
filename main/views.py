import imp
from unicodedata import name
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Course, Lesson, Solution, Task, Student, TaskStudent
from .forms import UploadFileForm
from django.contrib.auth.decorators import login_required
# Create your views here.

#HOME PAGE
def index(request):
    courses = Course.objects.all()
    if request.user.is_authenticated:
        user = request.user;
        student = Student.objects.get(user=user)
        tasks = TaskStudent.objects.all().filter(student=student)
        return render(request, "home.html", {"tasks": tasks, "courses": courses, "student": student})
    else:
        return render(request, "home.html", {"courses": courses})

@login_required(login_url='/login')
def remove_task_from_quickAccsses(request,id):
    user = request.user;
    student = Student.objects.get(user=user)
    task = TaskStudent.objects.get(student=student, task_id=id)

    task.quickA = False
    task.save()
    tasks = TaskStudent.objects.all().filter(student=student)
    courses = Course.objects.all()
    return render(request, "home.html", {"tasks": tasks, "courses": courses, "student": student})

@login_required(login_url='/login')
def tasks(request):
    user = request.user
    student = Student.objects.get(user=user)
    tasks = TaskStudent.objects.all().filter(student=student)
    courses = Course.objects.all()
    return render(request, "tasks.html", {"tasks": tasks, "courses": courses})

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
def task(request, taskid):
    form=UploadFileForm()
    user = request.user;
    student = Student.objects.get(user=user)
    courses = Course.objects.all()
    task = TaskStudent.objects.get(student=student, task_id=taskid)
    if(task.status!="Submited today"):
        task.status = "Opened today"
        task.save()

    
    if(Solution.objects.filter(student=student, task_id=taskid).exists()):
         solution = Solution.objects.get(student=student, task_id=taskid)
         print(solution.name)
         return render(request, "task.html", {"courses": courses, "studentTask": task, "form": form, "solution": solution})
    
    return render(request, "task.html", {"courses": courses, "studentTask": task, "form": form})

@login_required(login_url='/login')
def taskTrue(request, taskid):
    user = request.user;
    student = Student.objects.get(user=user)
    task = TaskStudent.objects.get(student=student, task_id=taskid)
    task.quickA=True
    task.save()
    return HttpResponse('')

@login_required(login_url='/login')
def taskFalse(request, taskid):
    user = request.user;
    student = Student.objects.get(user=user)
    task = TaskStudent.objects.get(student=student, task_id=taskid)
    task.quickA=False
    task.save()
    return HttpResponse('')
    
@login_required(login_url='/login')
def taskFinished(request, taskid):
    courses = Course.objects.all()
    user = request.user;
    student = Student.objects.get(user=user)
    task = TaskStudent.objects.get(student=student, task_id=taskid)
    form=UploadFileForm()
    if request.method == 'POST':
        form=UploadFileForm(request.POST, request.FILES)
        file=request.FILES['file']
        if(Solution.objects.filter(student=student, task_id=taskid).exists()):
            solution = Solution.objects.get(student=student, task_id=taskid);
            solution.delete()
        solution = Solution.objects.create(student=student, task_id=taskid, solution=file, name=file.name)
        print(solution.name)
        solution.save()
        form=UploadFileForm()
        task.status = "Submited today"
        task.save()
        return redirect('/tasks/' + str(taskid))
       
        
    return render(request, "task.html", {"courses": courses, "studentTask": task, "form": form, "solution": solution})

