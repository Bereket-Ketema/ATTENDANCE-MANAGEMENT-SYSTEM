import mysql.connector

# print("hello world")
def my():
    mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        password="1394",
        database="number"
    )
    # num1,num2=input().split()
    # num3=num1+num2
    num=int(input())
    mycursor=mydb.cursor()
    #mycursor.execute("CREATE TABLE number (id INT AUTO_INCREMENT PRIMARY KEY, number INT, nam
    # mycursor.execute("INSERT INTO numbers(num1,num2,result) VALUES (%s, %s,%s)",(num1,num2,num3))
    mycursor.execute("select * from numbers where num1=%s",[num])
    value=[]
    for data in mycursor:
        print(data)
    mydb.commit()
    # sql="select * from numbers"
    # mycursor.execute(sql)
    # result=mycursor.fetchall()

    # mycursor.execute("DESCRIBE numbers")
    # for data in mycursor:
    #     print(data)
    # for row in result:
    #     print(row)
    mycursor.close()
    mydb.close()


def teacher_login():
        db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="1394",
    database="attendance"
)
        user,passwords=input("Enter username and password: ").split()
        mycursor=db.cursor()
        mycursor.execute("SELECT t_id,password FROM teacher WHERE t_id = %s AND password= %s" ,[user,passwords])
        value=mycursor.fetchall()
        
        print (value[0][0])
        print(type(value[0][0]))
        
        db.commit()
        mycursor.close()
        db.close()

def student_sign():
    db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="1394",
    database="attendance"
)
    fname,lname,user,s_id,gender,passwords,dept=input().split()
    mycursor=db.cursor()
    mycursor.execute("INSERT INTO Student VALUES (%s,%s,%s,%s,%s,%s,%s)",(fname,lname,user,s_id,gender,passwords,dept))
    db.commit()
    print("inserted succesfully")
    mycursor.close()
    db.close()

def my():
     sec=[]
     yes(sec)
     for i in sec:
          print(i)
     
def yes(section):
    db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="1394",
    database="student"
)
    mycursor=db.cursor()
    mycursor.execute("show tables")
    for i in mycursor.fetchall():
            section.append(i[0])
    print(sum)
    db.commit()
    mycursor.close()
    db.close()
    return section

def secr():
    db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="1394",
    database="student"
)
    # sect="1"
    # sections="section"+sect
    mycursor=db.cursor()
    mycursor.execute("SELECT s_name,s_lname,s_id,gender,department FROM section1")
    section=[]
    sect=Are()
    print(len(section))
    for j in range(len(section)):
         for i in mycursor.fetchall():
            section.append(i)
         sect.s_name=section[j][0]
    print(sect.s_name)
    db.commit()
    mycursor.close()
    db.close()
class Are:
     s_name:str
     s_lname:str
     s_id:str
     gender:str
     department:str

def student_login():
    db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="1394",
    database="student"
)
    mycursor=db.cursor()
    mycursor.execute("SELECT * FROM {} ".format("section1"))
    values=mycursor.fetchall()
    print(values)
    values[0][0]
    db.commit()
    mycursor.close()
    db.close()
from first.models import Are

# Check if there are any records
print(Are.objects.all())
student_login()