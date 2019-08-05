from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from .forms import StudentRegistrationForm,Teachers_Signing_Form
from django.core.files.storage import FileSystemStorage

from .models import pdf_file
from .forms import uploadpdf 


# Create your views here.
