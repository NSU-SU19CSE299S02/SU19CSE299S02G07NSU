from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from .forms import StudentRegistrationForm,Teachers_Signing_Form
from django.core.files.storage import FileSystemStorage

from .models import pdf_file
from .forms import uploadpdf 

# This Function works for saving the student information into database

def studentform(request):
     if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            form.save()           
            return redirect('homepage')
	 else:
        form = StudentRegistrationForm()
        return render(request, 'studentform.html', {'form':form})

# This Function works for saving the Teacher information into database
def teacher_form(request):
     if request.method == 'POST':
        form = Teachers_Signing_Form(request.POST)
		if form.is_valid():
            form.save()           
            return redirect('homepage')
	   else:
        form = Teachers_Signing_Form()
        return render(request, 'teacher_signing_form.html', {'form':form})

# This function works for student Login
def student_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
		if user:
             login(request, user)
             return redirect("mainpage")
          
        else:
             return render(request, "home.html")