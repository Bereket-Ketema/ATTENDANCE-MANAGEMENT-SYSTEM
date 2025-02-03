from django.db import models

# Create your models here.

class Use(models.Model):
    fname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    users=models.CharField(max_length=100)
    s_id=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)
    passwords=models.CharField(max_length=100)
    dept=models.CharField(max_length=100)
    sect=models.CharField(max_length=100)
    def __str__(self):
        return self.fname,self.lname,self.users,self.gender,self.passwords,self.dept,self.sect

class Section(models.Model):
    name=models.CharField(max_length=100)

class Are(models.Model):
     s_name=models.CharField(max_length=100)
     s_lname=models.CharField(max_length=100)
     s_id=models.CharField(max_length=100)
     gender=models.CharField(max_length=100)
     password=models.CharField(max_length=100)
     department=models.CharField(max_length=100)
     def __str__(self):
        return self.s_name

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name