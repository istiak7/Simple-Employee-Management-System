from django.shortcuts import render , redirect
from django.http import HttpResponse
from .forms import EmployeeForm ,EmployeeUpdateForm, CustomUserCreationForm
from .models import Employee
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout,authenticate 
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
# Create your views here.


def registration(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:form = CustomUserCreationForm()
    return render(request,'register_employee.html',{'form':form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect(request.GET.get('next','display'))
    else:
        form = AuthenticationForm()
    return render(request,'login_employee.html',{'form':form})

def logout_view(request):
        logout(request)
        return redirect('demo')

def display_employee(request):
    employee_data = Employee.objects.all()
    return render(request,'employee_list.html',{'employee_data':employee_data})
def display_employee_details(request,pk):
    employee_data = Employee.objects.get(pk=pk)
    return render(request,'employee_details.html',{'employee_data':employee_data})

@login_required
def add_employee(request):
    if request.method == 'POST':
          form = EmployeeForm(request.POST)
          if form.is_valid():
                form.save()
                return redirect(request.GET.get('next','display'))
          else:return render(request,'index.html',{'form':form})
    else: form = EmployeeForm()
    return render(request,'index.html',{'form':form})

def update(request):
    employee_data = Employee.objects.all()
    return render(request,'employee_update_list.html',{'employee_data':employee_data})

@login_required
def update_employee(request,pk):
    try:
        employee_data = Employee.objects.get(pk=pk)
        
        if request.method == 'POST':
            form = EmployeeUpdateForm(request.POST,instance = employee_data)#data akhane immutable
            if 'disabled' in form.fields['designation'].widget.attrs:
                del form.fields['designation'].widget.attrs['disabled']
            form.data = form.data.copy()  # Make POST data mutable
            form.data['designation'] = employee_data.designation
            if form.is_valid():
                form.save()
                return redirect(request.GET.get('next','display'))
            else:
                return render(request, 'employee_update.html', {'form': form})
 
        else:
            form = EmployeeUpdateForm(instance=employee_data)
            form.fields['salary'].widget.attrs['readonly'] = True
            form.fields['designation'].widget.attrs['disabled'] = 'disabled'
            return render(request,'employee_update.html',{'form':form})
    except Employee.DoesNotExist:
        return HttpResponse('Employee Doesnot Exist.')
@login_required
def delete_employee(request,pk):
    try:
        employee_data = Employee.objects.get(pk=pk)
        employee_data.delete()
        return redirect('display')
    except Employee.DoesNotExist:
        return HttpResponse("Employee Doesnot Exist")
    
def delete(request):
    employee_data = Employee.objects.all()
    return render(request,'employee_delete_list.html',{'employee_data':employee_data})

def demo_view(request):
    return render(request,'demo.html')