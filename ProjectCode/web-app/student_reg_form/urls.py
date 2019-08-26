from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
	path('', views.success, name = "homepage"),
    path('studentform/', views.studentform, name='student_form'),
    path('teacherform/', views.teacher_form, name='TeacherForm'),
    path('login/', views.student_login, name ="login"),
   

]

