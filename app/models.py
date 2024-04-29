from django.db import models

# Create your models here.
class Course(models.Model):
    CID=models.IntegerField(primary_key=True)
    Cname=models.CharField(max_length=100,null=False)
    Fees=models.IntegerField()
    Tname=models.CharField(max_length=100)

    def __str__(self):
        return (self.Cname)

class Student(models.Model):
    SID=models.IntegerField(primary_key=True)
    Sname=models.CharField(max_length=100,unique=True)
    Age=models.IntegerField()
    DOB=models.DateField()
    Gender=models.CharField(max_length=100)
    CID=models.ForeignKey(Course,on_delete=models.CASCADE)

    def __str__(self):
        return (self.Sname)



