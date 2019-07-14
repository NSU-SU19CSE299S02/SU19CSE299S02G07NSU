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
     def save(self, commit = True):
        user = super(StudentRegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user
		
		# This class for Teacher registration form which data saved into database
class Teachers_Signing_Form(forms.ModelForm):