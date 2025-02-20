from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
import mysql.connector
from .models import  Item, Section, Use,Are
# Create your views here.
def welcome(request):
    return render(request,'welcome.html')
def login(request):
    return render(request,'login.html')
def teachers(request):
    return render(request,'teacher.html')
def stud(request):
    return render(request,'student.html')
def teach(request):
    return render(request,'t_sign.html')
def study(request):
    return render(request,'s_sign.html')
def stud_log(request):
    return render(request,'s_login.html')
def about(request):
    return render(request,'about.html')
def t_login(request):
    return render(request,'t_login.html')
def student_login(request):
    if request.method == "POST":
        # Get the submitted password
        learner = Use.objects.filter(passwords=request.POST.get("pass"))
        if learner.exists():
            learn= Use.objects.get(passwords=request.POST.get("pass")) # Check if the query returned any results
            return render(request, 's_data.html',{'learner':learn}) # Redirect to section page
        else:
            return render(request, 's_login.html', {'error': "Incorrect username or password"})
    else:
        return render(request, 's_login.html')  # Render the login page for GET requests
    
def teacher_login(request):
    if request.method == "POST":
        # Get the submitted password
        # Validate if the password exists in the database
        assistant = Are.objects.filter(passwordss=request.POST.get("passwordss"))
        if assistant.exists():  # Check if the query returned any results
            return render(request, 'section.html')  # Redirect to section page
        else:
            return render(request, 't_login.html', {'error': "Incorrect username or password"})
    else:
        return render(request, 't_login.html')  # Render the login page for GET requests

def teacher(request):
  if request.method=='POST':
    teache=Are(t_name=(request.POST['fname']),t_lname=(request.POST['lname']),
             t_id=(request.POST['t_id']),gender=(request.POST['gender']),passwordss=(request.POST['passwords']),
             department=(request.POST['department']))
    teache.save()
    return render(request,'t_login.html')
  return render(request,'t_sign.html')

def student_sign(request):
  if request.method=='POST':
    stud=Use(
        fname=(request.POST['fname']),lname=(request.POST['lname']), users=(request.POST['user']),
             s_id=(request.POST['id']),gender=(request.POST['gender']),passwords=(request.POST['passwords']),
             dept=request.POST['department'],sect=(request.POST['section'])
    )
    stud.save()
    return render(request,'s_login.html')
  return render(request,'s_sign.html')


##########################################

def section(request):
 if request.method=='POST':
    sections=Use.objects.filter(sect=request.POST['section'])
    return render(request, 'data.html',{'person':sections})


