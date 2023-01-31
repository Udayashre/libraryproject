from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, redirect

from libraryApp.models import Student, Course, Book, Issue_Book


def login_fun(request):
    return render(request,'login.html',{'data':''})


def logdata_fun(request):
    if request.method == 'POST':
      names=request.POST['txtUserName']
      Password = request.POST['txtPassword']

      user1 = authenticate(username = names,password = Password)
      if user1 is not None:
        if user1.is_superuser:
            login(request,user1)
            request.session['u_name']= request.POST['txtUserName']
            return redirect('ahome')
        else:
            return render(request,'login.html',{'data':'user is not a superuser'})
      elif Student.objects.filter(Q(StudentName = names) & Q(Password = Password)).exists():
              request.session['u_name']=names
              return render(request,'studenthome.html',{'studata':request.session['u_name']})
      else:
        return render(request,'login.html',{'data':'enter proper username and password'})
    else:
        return render(request,'login.html',{'data':''})

def admin_fun(request):
    return render(request,'admin registration.html',{'data':''})


def admindata_fun(request):
    adminname=request.POST['txtAdminName']
    email=request.POST['txtEmail']
    password=request.POST['txtPassword']
    if User.objects.filter(Q(username=adminname)| Q(email=email)).exists():
       return render(request,'admin registration.html',{'adata':'name and email is already exists'})

    else:
       u1= User.objects.create_superuser(username=adminname,email=email,password=password)
       u1.save()
       return redirect('log')

def studata_fun(request):
        s1 = Student()
        s1.studentName = request.POST['txtStudentName']
        s1.Pno = request.POST['txtPno']
        s1.Semester = request.POST['txtSemester']
        s1.Password = request.POST['txtPassword']
        s1.Course_id = Course.objects.get(course_name=request.POST['ddlCourse'])
        s1.save()
        return redirect('log')


def student_fun(request):
    course  = Course.objects.all()
    return render(request,'student registration.html',{'data':'','course':course})


def adminhome_fun(request):
    return render(request,'adminhome.html')


def stuhome_fun(request):
    return render(request,'studenthome.html')


def addbook_fun(request):
    b1 = Book()
    b1.Book_Name = request.POST['txtBookName']
    b1.Author_Name = request.POST['txtAuthorName']
    b1.course_id = Course.objects.get(course_name=request.POST['ddlCourse'])
    b1.save()
    return redirect('add')


def book_fun(request):
    course = Course.objects.all()
    return render(request,'addbook.html',{'Course_Data':course})


def display_fun(request):
    b1 = Book.objects.all()
    return render(request,'display book.html',{'data':b1})


def update_fun(request,id):
    b1 = Book.objects.get(id=id)
    course = Course.objects.all()

    if request.method == 'POST':
        b1.Book_Name = request.POST['txtBookName']
        b1.Author_Name = request.POST['txtAuthorName']
        b1.course_id = Course.objects.get(course_name=request.POST['ddlCourse'])
        b1.save()
        return redirect('displaybook')
    return render(request,'update.html',{'data':b1,'Course_Data':course})


def delete_fun(request,id):
    b1 = Book.objects.get(id=id)
    b1.delete()
    return redirect('displaybook')


def log_out_fun(request):
    return redirect('log')


def assignbook_fun(request):
    course = Course.objects.all()
    return render(request,'assignbook.html',{'course':course,'student':'','book':''})


def assigndata_fun(request):
     stu = Student.objects.filter(Q(Semester=request.POST['txtsemester']) & Q(course_id=Course.objects.get(course_name=request.POST['ddlcourse'])))
     book = Book.objects.filter(course_id=Course.objects.get(course_name=request.POST['ddlcourse']))
     return render(request,'assignbook.html',{'Student':stu,'Book':book})



def issueread_fun(request):
    i1 = Issue_Book()
    i1.Student_Name = Student.objects.get(StudentName=request.POST['ddlstudentname'])
    i1.Book_Name = Book.objects.get(Book_Name=request.POST['ddlbook_name'])
    i1.Start_Date = request.POST['startdate']
    i1.End_Date = request.POST['enddate']
    i1.save()
    return redirect('assignbook')




def updateissue_fun(request,id):
    i1 = Issue_Book.objects.get(id=id)
    student = Student.objects.get(id=i1.Student_Name_id)
    book = Book.objects.filter(Course_id=student.course_id)

    if request.method =='POST':

        i1.Student_Name = Issue_Book.objects.get(Student_Name=request.POST['ddlStudent_Name'])
        i1.Book_Name = Issue_Book.objects.get(Book_Name=request.POST['ddlbook_name'])
        i1.Start_Date = request.POST['startdate']
        i1.End_Date = request.POST['enddate']
        i1.save()
        return redirect('issuebook')
    return render(request,'issueupdate.html',{'data':i1,'Book':book})

def delete_issue(request,id):
    i1 = Issue_Book.objects.get(id=id)
    i1.delete()
    return redirect('issuebook')


def issuebook_fun(request):
    i1 = Issue_Book.objects.all()
    return render(request,'issuebook.html',{'ddata':i1})



def issuedetail_fun(request):
    i1=Issue_Book.objects.filter(Student_Name=Student.objects.get(StudentName=request.session['u_name']))
    return render(request,'issuedetails.html',{'ddata':i1})


def profile_fun(request):
    s1=Student.objects.get(StudentName=request.session['u_name'])
    return render(request,'profile.html',{'data':s1})


def updateprof_fun(request,id):
    s1=Student.objects.get(id=id)
    if request.method == 'POST':
        s1.studentName = request.POST['txtStudentName']
        s1.Pno = request.POST['txtPno']
        s1.Semester = request.POST['txtSemester']
        s1.Password = request.POST['txtPassword']
        s1.save()
        return redirect('profile')
    return render(request,'update_prof.html',{'data':s1})