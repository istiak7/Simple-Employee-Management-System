from django import forms
from .models import Employee
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm 
import re

SOFTWARE = 'Software Engineer'
DEVELOPER = 'Django Developer'
DESIGNER = 'UI/UX Designer'
SQA = 'Software Quality Assurance'

DESIGNATION_CHOICES = [
    (SOFTWARE, 'Software Engineer'),
    (DEVELOPER, 'Django Developer'),
    (DESIGNER, 'UI/UX '),
    (SQA, 'Software Quality Assurance'),
    ]

class EmployeeForm(forms.ModelForm):
   
    designation = forms.ChoiceField(
        choices=DESIGNATION_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=True
    )

    class Meta:
        model = Employee
        fields = '__all__' 

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if not phone_number.startswith('+88'):
            raise ValidationError("Phone number must start with '+88'.")
        actual_number = phone_number[3:]
        if not actual_number.isdigit() or len(actual_number) != 11:
            raise ValidationError("The phone number must contain exactly 11 digits after the '+88'.")

        return phone_number
    def clean_salary(self):
        salary = self.cleaned_data.get('salary')
        if salary >= 0.01:
            return salary
        raise ValidationError("Salary must Greater that 0")
    def clean_Employee_Id(self):
        employee_id = self.cleaned_data['Employee_Id']
        employee_ids = list(Employee.objects.values_list('Employee_Id', flat=True))
        if employee_id in employee_ids:
            raise ValidationError("This Id is Already Given!")
        return employee_id
class EmployeeUpdateForm(forms.ModelForm):
   
    designation = forms.ChoiceField(
        choices=DESIGNATION_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=True
    )

    class Meta:
        model = Employee
        fields = '__all__' 

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if not phone_number.startswith('+88'):
            raise ValidationError("Phone number must start with '+88'.")
        actual_number = phone_number[3:]
        if not actual_number.isdigit() or len(actual_number) != 11:
            raise ValidationError("The phone number must contain exactly 11 digits after the '+88'.")

        return phone_number
    def clean_salary(self):
        salary = self.cleaned_data.get('salary')
        if salary >= 0.01:
            return salary
        raise ValidationError("Salary must Greater that 0")
  
    
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username','first_name','last_name','email','password1','password2'
        ]
    def save(self, commit = True):
        user = super().save(commit = False) #user r object create koro but save koiro na
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit: 
            user.save()
        return user
    