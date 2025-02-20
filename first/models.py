from django.db import models

# Create your models here.

class Use(models.Model):
    fname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    users=models.CharField(max_length=100,primary_key=True)
    s_id=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)
    passwords=models.CharField(max_length=100)
    dept=models.CharField(max_length=100)
    sect=models.CharField(max_length=100)
    def __str__(self):
        return self.fname,self.lname,self.users,self.gender,self.passwords,self.dept,self.sect

class Section(models.Model):
    name=models.CharField(max_length=100,primary_key=True)

class Are(models.Model):
     t_name=models.CharField(max_length=100)
     t_lname=models.CharField(max_length=100)
     t_id=models.CharField(max_length=100,primary_key=True)
     gender=models.CharField(max_length=100)
     passwordss=models.CharField(max_length=100)
     department=models.CharField(max_length=100)
     def __str__(self):
        return self.t_name,self.t_lname,self.gender,self.passwordss,self.department

class Item(models.Model):
    name = models.CharField(max_length=100,primary_key=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name