from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tasks', views.tasks, name='tasks'),
    path('Illustration', views.illustrationCourse, name='illustrationCourse'),
    path('Illustration/<str:lessonName>', views.illustration_lesson, name="illustration_lesson"),
    path('Typography', views.typographyCourse, name='typography' ),
    path('Typography/<str:lessonName>', views.typography_lesson, name="typography_lesson"),
    path('Photography', views.photographyCourse, name='photography'),
    path('Photography/<str:lessonName>', views.photography_lesson, name="photography_lesson"),
    path('tasks/<int:taskid>', views.task, name="task"),
    path('tasks/<int:taskid>/true', views.taskTrue, name="taskTrue"),
    path('tasks/<int:taskid>/false', views.taskFalse, name="taskFalse"),
    path('tasks/<int:taskid>/submit', views.taskFinished, name="taskFinished"),
    path('<int:id>', views.remove_task_from_quickAccsses, name="remove_task_from_quickAccsses"),
    
] 
