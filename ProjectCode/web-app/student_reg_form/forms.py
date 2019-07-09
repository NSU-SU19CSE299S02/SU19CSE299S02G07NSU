from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# This class for student registration form which data saved into database
class StudentRegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = {
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        }
    