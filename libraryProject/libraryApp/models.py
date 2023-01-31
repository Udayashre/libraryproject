from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Course(models.Model):
    course_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.course_name}"

class Book(models.Model):
    Book_Name = models.CharField(max_length=50)
    Author_Name = models.CharField(max_length=50)
    course_id = models.ForeignKey(Course,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.Book_Name}"



class Student(models.Model):
    StudentName = models.CharField(max_length=50)
    Password = models.CharField(max_length=50)
    Pno = models.BigIntegerField()
    Semester = models.IntegerField()
    course_id = models.ForeignKey(Course,on_delete=models.CASCADE)

    def __str__(self):
          return f"{self.StudentName}"

class Issue_Book(models.Model):
    Student_Name = models.ForeignKey(Student, on_delete=models.CASCADE)
    Book_Name = models.ForeignKey(Book,on_delete=models.CASCADE)
    Start_Date = models.DateField()
    End_Date = models.DateField()

