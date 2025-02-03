from django.http import HttpResponse
from django.shortcuts import redirect, render
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

#student login
def student_login(request):
    db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="1394",
    database="student"
)
    studs=Use()
    studs.users=request.GET['users']
    studs.passwords=request.GET['pass']
    studs.sect=request.GET['section']
    sections="section"+studs.sect
    mycursor=db.cursor()
    mycursor.execute("SELECT s_name,s_lname,department FROM {} WHERE user = %s AND password= %s".format(sections) ,[studs.users,studs.passwords])
    values=mycursor.fetchall()
    db.commit()
    mycursor.close()
    db.close()
    if(len(values)>0):
        studs.fname=values[0][0]
        studs.lname=values[0][1]
        studs.dept=values[0][2]
        return render(request,'s_data.html',{'studs':studs})
    else:
        return render(request,'s_login.html',{'error':"Incorrect username or password"})
    

#Teacher sign
def teacher(request):
    db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="1394",
    database="attendance"
)
 
    if request.method == 'GET':
        teacher=Use()
        teacher.fname=(request.GET['fname'])
        teacher.lname=(request.GET['lname'])
        teacher.users=(request.GET['t_id'])
        teacher.gender=(request.GET['gender'])
        teacher.passwords=(request.GET['passwords'])
        teacher.dept=(request.GET['department'])
        mycursor=db.cursor()
        mycursor.execute("INSERT INTO Teacher VALUES (%s, %s,%s,%s, %s,%s)",(teacher.fname,teacher.lname,teacher.users,teacher.gender,teacher.passwords,teacher.dept))
        db.commit()
        mycursor.close()
        db.close()
        #Redirect to the view page after submission
        return render(request,'t_login.html')
    return render(request,'t_sign.html')

#Student sign_up
def student_sign(request):
    db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="1394",
    database="student"
)
    student=Use()
    student.fname=(request.GET['fname'])
    student.lname=(request.GET['lname'])
    student.users=(request.GET['user'])
    student.gender=(request.GET['gender'])
    student.passwords=(request.GET['passwords'])
    student.dept=(request.GET['department'])
    student.s_id=(request.GET['id'])
    student.sect=request.GET['section']
    sections="section"+student.sect
    mycursor=db.cursor()
    mycursor.execute("INSERT INTO {} VALUES (%s,%s,%s,%s,%s,%s,%s)".format(sections),(student.fname,student.lname,student.users,student.s_id,student.gender,student.passwords,student.dept))
    db.commit()
    mycursor.close()
    db.close()
    return render(request,'s_login.html')

def t_login(request):
    names=Use()
    names.fname="Bereket"
    return render(request,'t_login.html',{'names':names.fname})

#teacher login
def teacher_login(request):
        db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="1394",
    database="attendance"
)
        sec=[]
        users=request.GET['t_ids']
        passwords=request.GET['passwordss']
        mycursor=db.cursor()
        mycursor.execute("SELECT t_id,password FROM teacher WHERE t_id = %s AND password= %s" ,[users,passwords])
        values=mycursor.fetchall()
        db.commit()
        mycursor.close()
        db.close()
        if request.method == 'GET':
            if(len(values)>0):
                sections(sec)
                return render(request,'section.html',{'sections':sec})
        return render(request,'t_login.html')  

def section(request):
    section=Section()
    return render(request,'section.html',{'section':section})

def sec(request):
    db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="1394",
    database="student"
)
    studs=Use()
    studs.sect=request.GET['section']
    studs.sect=str(studs.sect)
    sections="section"+studs.sect
    mycursor=db.cursor()
    mycursor.execute("SELECT s_name,s_lname,s_id,gender,department FROM {}".format(sections))
    sect=Are()
    secs=[]
    for i in mycursor.fetchall():
        i=i[0]
        secs.append(i)
    db.commit()
    mycursor.close()
    db.close()
    return render(request,'data.html',{"section":sect})
    
def sections(sec):
    db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="1394",
    database="student"
)
    mycursor=db.cursor()
    mycursor.execute("show tables")
    for i in mycursor.fetchall():
        sec.append(i[0]) 
    db.commit()
    mycursor.close()
    db.close()
    return sec

# def chk(request):
#     db=mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="1394",
#     database="student"
# )
#     mycursor=db.cursor()
#     mycursor.execute("SELECT s_name,s_lname,s_id,gender,department FROM {} ".format("section1"))
#     values=mycursor.fetchall()
#     db.commit()
#     mycursor.close()
#     db.close()
#     return render(request,"data.html",{"values":values})



def item_list(request):
    items = Use.objects.all()  # Fetch all records from the Item table
    return render(request, 'data.html', {'items': items})